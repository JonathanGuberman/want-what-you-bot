from string import digits

syllabifications = None

def init(filename="cmudict.0.6-syl"):
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
  return syllabifications.get(word)