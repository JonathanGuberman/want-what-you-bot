from collections import defaultdict
from enum import Enum, auto
import random
from syllabifications import get_syllables

class PartsOfSpeech(Enum):
  NOUN = auto()
  ADJECTIVE = auto()

class WordChoices:
  def __init__(self, wordlists):
      self.mononoun1, self.mononoun2 = random.sample(wordlists[(PartsOfSpeech.NOUN, 1)], 2)
      self.trocheenoun1, self.trocheenoun2 = random.sample(wordlists[(PartsOfSpeech.NOUN, 2)], 2)
      self.amphinoun1, self.amphinoun2 = random.sample(wordlists[(PartsOfSpeech.NOUN, 3)], 2)
      self.adj = random.choice(wordlists[(PartsOfSpeech.ADJECTIVE, 1)])


def random_lyrics(words):
  lyrics = f'''
  I want your {words.trocheenoun1}
  I want your {words.trocheenoun2}
  I want what you got, I say it a lot
  I want your {words.adj} {words.mononoun1}
  Want your {words.amphinoun1}
  I want what you got, I say it a lot
  Oh my god, oh my god, oh my god, oh my god
  I want what you got, I say it a lot
  I want your {words.mononoun2}, I
  Want your {words.amphinoun2}
  I want what you got, I say it a lot
  '''
  return lyrics

def singing_xml(words):
  xml = f'''
  <!DOCTYPE SINGING PUBLIC "-//SINGING//DTD SINGING mark up//EN"
      "Singing.v0_1.dtd">
<SINGING BPM="112">
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.trocheenoun1)[0]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.trocheenoun1)[1]}</DURATION></PITCH>
<REST BEATS="1.0"></REST>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.trocheenoun2)[0]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.trocheenoun2)[1]}</DURATION></PITCH>
<REST BEATS="1.0"></REST>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{words.adj}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{words.mononoun1}</DURATION></PITCH>
<REST BEATS="1.0"></REST>
<PITCH NOTE="A4"><DURATION BEATS="0.5">{get_syllables(words.amphinoun1)[0]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.amphinoun1)[1]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="0.5">{get_syllables(words.amphinoun1)[2]}</DURATION></PITCH>
<REST BEATS="1.0"></REST>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{words.mononoun2}</DURATION></PITCH>
<REST BEATS="1.0"></REST>
<PITCH NOTE="A4"><DURATION BEATS="0.5">{get_syllables(words.amphinoun2)[0]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.0">{get_syllables(words.amphinoun2)[1]}</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="0.5">{get_syllables(words.amphinoun2)[2]}</DURATION></PITCH>
</SINGING>
  '''
  return xml

def file_to_list(filename):
  with open(filename) as fp:
    return [line.strip() for line in fp]

if __name__ == "__main__":
  wordlists = defaultdict(list, {
    (PartsOfSpeech.NOUN, 1): file_to_list("./wordlists/NN-1.txt"),
    (PartsOfSpeech.NOUN, 2): file_to_list("./wordlists/NN-2.txt"),
    (PartsOfSpeech.NOUN, 3): file_to_list("./wordlists/NN-3.txt"),
    (PartsOfSpeech.ADJECTIVE, 1): file_to_list("./wordlists/JJ-1.txt"),
  } )

  word_choices = WordChoices(wordlists)
  print(random_lyrics(word_choices))
  print()
  print(singing_xml(word_choices))