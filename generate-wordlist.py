import nltk
from nltk.corpus import brown
import pronouncing

from collections import defaultdict

pronouncing.init_cmu()

print("Building syllable count DB")
# sylcount = {}
# for word, phones in pronouncing.pronunciations:
#     if word in sylcount: continue
#     sylcount[word] = pronouncing.syllable_count(phones)

ones = pronouncing.search_stresses("^1$")
twos = pronouncing.search_stresses("^1[02]$")
threes = pronouncing.search_stresses("^[02]1[02]$")

sylcount = dict.fromkeys(ones, 1)
sylcount.update(dict.fromkeys(twos, 2))
sylcount.update(dict.fromkeys(threes, 3))

print("Counting syllables")
by_pos_count = defaultdict(set)
for word, tag in brown.tagged_words():
    if word[0].isupper() and not tag.startswith("NP"):
        continue
    tag = tag.split('-')[0]
    if tag not in ("NN", "NNS", "JJ"): 
      continue
    tag = tag[:2]
    try:
        count = sylcount[word.lower()]
    except:
        continue
    by_pos_count[tag, count].add(word)

print("Writing output")
for tag, count in by_pos_count.keys():
    filename = "wordlists/%s-%d.txt" % (tag, count)
    with open(filename, "w") as f:
        for word in sorted(by_pos_count[tag, count]):
            f.write(word + "\n")