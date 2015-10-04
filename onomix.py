import os
from multiprocessing import Process
from string import ascii_lowercase

import whois

import util.opt_parser as parser
from util.toolkit import log, PermutationIterator


def run_name(name):
    try:
        whois.query(name)
        log.info("[" + str(os.getpid()) + "] " + name + " [TAKEN]")
    except (Exception):
        log.info("[" + str(os.getpid()) + "] " + name + " [FREE]")


for e in PermutationIterator(ascii_lowercase, int(parser.options.length)):
    name = "".join(e) + parser.options.tld
    result = None

    # log.debug("Trying: " + name)

    p = Process(target=run_name, args=(name,))
    p.start()
    p.join()
