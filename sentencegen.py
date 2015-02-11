'''
Generate random sentences
'''

import math
from random import SystemRandom

def read_wordlists():
    '''Reads a set of files named [element]s.txt in the same directory'''
    filenames = [ "adjective", "adverb", "noun",
                  "preposition", "pronoun", "verb"]
    wordlists = {}
    for f in filenames:
        wordlists[f] = [l.strip() for l in open("{}s.txt".format(f)).readlines()]
    return wordlists

def measure_entropy(template, element_map):
    return int(sum(map(lambda x: math.log(len(element_map[x]), 2), template)))

def generate_sentence(template, element_map):
    return map(lambda x: SystemRandom().sample(element_map[x], 1)[0], template)

example_templates = [[ "preposition", "pronoun", "noun", "adverb",
                       "verb", "adjective", "noun"],
                     [ "adjective", "noun", "adverb",
                       "verb", "preposition", "pronoun", "noun"],
                     [ "adverb", "verb", "preposition",
                       "adjective", "noun", "preposition", "noun"]]

wordlists = read_wordlists()
print "\tEstimated entropy: {}".format(
    map(lambda x: measure_entropy(x, wordlists), example_templates))

for i in xrange(10):
    rand_template = SystemRandom().sample(example_templates, 1)[0]
    print "\t{}".format(" ".join(generate_sentence(rand_template, wordlists)))
