import os
from multiprocessing import Pool
from string import ascii_lowercase
import itertools

import whois

import util.opt_parser as parser
from util.toolkit import log, PermutationIterator

if __name__ == '__main__':
    def calculate_permutations(character_list, length):
        d = []
        for p in itertools.permutations(character_list, length):
            d.append(''.join(p))
        return len(d)


    def run_name(domain_name):
        try:
            q = whois.query(domain_name)
            print q
            log.info("[" + str(os.getpid()) + "] " + domain_name + " [TAKEN]")
        except (Exception):
            log.info("[" + str(os.getpid()) + "] " + domain_name + " [FREE]")


    log.info("Permutations are " + str(calculate_permutations(ascii_lowercase, int(parser.options.length))))

    p = Pool(10)
    for e in PermutationIterator(ascii_lowercase, int(parser.options.length)):
        domain_name = str("".join(e) + parser.options.tld)
        result = None

        log.debug("Trying: " + domain_name)

        p.apply(run_name, args=(domain_name,))
