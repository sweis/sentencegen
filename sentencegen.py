'''
Generate random sentences
'''

import math
import random  # For demo only.

elements = [ "adjective", "adverb", "noun",
             "preposition", "pronoun", "verb"]

def measure_entropy(template, element_map):
    return int(sum(map(lambda x: math.log(len(element_map[x]), 2), template)))

def generate_sentence(template, element_map):
    return map(lambda x: random.sample(element_map[x], 1)[0], template)

elem_map = {}
for e in elements:
    # This is expecting files named [element]s.txt in the same directory
    elem_map[e] = [l.strip() for l in open("{}s.txt".format(e)).readlines()]

example_template = [ "preposition", "adjective", "noun", "adverb",
                     "adjective", "noun"]

print "Example template:", " ".join(example_template)
print "Entropy:", measure_entropy(example_template, elem_map)
print "Samples:"
for i in xrange(10):
    print "\t", " ".join(generate_sentence(example_template, elem_map))
