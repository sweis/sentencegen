'''
Generate random sentences
'''

import math
import random  # For demo only.


def read_word_sources():
    '''Reads a set of files named [element]s.txt in the same directory'''
    filenames = [ "adjective", "adverb", "noun",
                  "preposition", "pronoun", "verb"]
    elem_map = {}
    for f in filenames:
        elem_map[f] = [l.strip() for l in open("{}s.txt".format(f)).readlines()]
    return elem_map

def measure_entropy(template, element_map):
    return int(sum(map(lambda x: math.log(len(element_map[x]), 2), template)))

def generate_sentence(template, element_map):
    return map(lambda x: random.sample(element_map[x], 1)[0], template)


example_template = [ "preposition", "adjective", "noun", "adverb",
                     "adjective", "noun"]

wordlists = read_word_sources()

print "Example template:", " ".join(example_template)
print "Entropy:", measure_entropy(example_template, wordlists)
print "Samples:"
for i in xrange(10):
    print "\t", " ".join(generate_sentence(example_template, wordlists))
