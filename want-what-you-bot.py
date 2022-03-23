import random

class CategorizedWords:
  def __init__(self, nouns, adjectives):
    self.nouns = nouns
    self.adjectives = adjectives

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

def file_to_list(filename):
  with open(filename) as fp:
    return [line.strip() for line in fp]

if __name__ == "__main__":
  ones = file_to_list("./wordlists/NN-1.txt")
  twos = file_to_list("./wordlists/NN-2.txt")
  threes = file_to_list("./wordlists/NN-3.txt")
  adj = file_to_list("./wordlists/JJ-1.txt")

  print(random_lyrics(CategorizedWords([ones, twos, threes], adj)))