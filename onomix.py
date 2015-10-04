import whois
import sys
import util.opt_parser as parser
from string import ascii_lowercase
from util.toolkit import log

dn = ''

def permutation_atindex(_int, _set, length):
    """
    Return the permutation at index '_int' for itemgetter '_set'
    with length 'length'.
    """
    items = []
    strLength = len(_set)
    index = _int % strLength
    items.append(_set[index])

    for n in xrange(1,length, 1):
        _int //= strLength
        index = _int % strLength
        items.append(_set[index])

    return items

class PermutationIterator:
    """
    A class that can iterate over possible permuations
    of the given 'iterable' and 'length' argument.
    """

    def __init__(self, iterable, length):
        self.length = length
        self.current = 0
        self.max = len(iterable) ** length
        self.iterable = iterable

    def __iter__(self):
        return self

    def next(self):
        if self.current >= self.max:
            raise StopIteration

        try:
            return permutation_atindex(self.current, self.iterable, self.length)
        finally:
            self.current   += 1

log.debug("starting... ")

for e in PermutationIterator(ascii_lowercase, int(parser.options.length)):
    name = "".join(e) + parser.options.tld
    result = None


    print ("Trying: " + name),

    try:
        result = whois.query(name)
        print "[TAKEN]"
    except (Exception):
        print "[FREE]"






