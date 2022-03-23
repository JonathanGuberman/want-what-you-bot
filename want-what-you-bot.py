from collections import defaultdict
import random

from nltk.corpus import cmudict as cmu, wordnet as wn

class CategorizedWords:
  def __init__(self, wordlist):
    self.syllable_map = defaultdict(list)
    self.nouns = [[], [], []]
    self.adjectives = []

    for word in wordlist:
      stress_pattern = syllables(word)
      if stress_pattern:
        self.syllable_map[syllables(word)].append(word)

        if wn.synsets(word, pos=wn.NOUN):
          if stress_pattern == (1,):
            self.nouns[0].append(word)
          elif stress_pattern == (1, 0) or stress_pattern == (1,2):
            self.nouns[1].append(word)
          elif stress_pattern == (0, 1, 0):
            self.nouns[2].append(word)
        elif wn.synsets(word, pos=wn.ADJ):
          if stress_pattern == (1,):
            self.adjectives.append(word)


CMUDICT = cmu.dict()

def syllables(word):
  # return tuple(int(s[-1]) for s in cmudict[word.lower()] if s[-1].isdigit())
  if word.lower() in CMUDICT:
    return tuple(int(s[-1]) for s in CMUDICT[word.lower()][0] if s[-1].isdigit())
  return None

def random_lyrics(categorized_words):
  lyrics = f'''
  I want your {random.choice(categorized_words.nouns[1])}
  I want your {random.choice(categorized_words.nouns[1])}
  I want what you got, I say it a lot
  I want your {random.choice(categorized_words.adjectives)} {random.choice(categorized_words.nouns[0])}
  Want your {random.choice(categorized_words.nouns[2])}
  I want what you got, I say it a lot
  Oh my god, oh my god, oh my god, oh my god
  I want what you got, I say it a lot
  I want your {random.choice(categorized_words.nouns[0])}, I
  Want your {random.choice(categorized_words.nouns[2])}
  I want what you got, I say it a lot
  '''
  return lyrics

if __name__ == "__main__":
  with open("20k.txt") as wordfile:
    wordlist = [word.strip() for word in wordfile]

  print(random_lyrics(CategorizedWords(wordlist)))