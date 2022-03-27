from string import digits

syllabifications = None

def init(filename="wordlists/cmudict.0.6-syl"):
  global syllabifications
  if syllabifications is None:
    syllabifications = {}
    with open(filename) as fp:
      for line in fp:
        line = line.strip().lower()
        if not line or line.startswith("##"):
          continue
        word, syllabification = line.split("  ")
        syllabifications[word] = syllabification.translate(str.maketrans('', '', digits + " ")).split(".")

def get_syllables(word):
  init()
  syllabification = syllabifications.get(word)
  if syllabification:
    return syllabification
  if word[-1] == 's':
    singular = syllabifications.get(word[:-1])
    plural = singular.copy()
    plural[-1] += 'z'
    return plural

  return None