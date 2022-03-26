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
  lyrics = (
    f'I want your {words.trocheenoun1}\n'
    f'I want your {words.trocheenoun2}\n'
    f'I want what you got, I say it a lot\n'
    f'I want your {words.adj} {words.mononoun1}\n'
    f'Want your {words.amphinoun1}\n'
    f'I want what you got, I say it a lot\n'
    f'Oh my god ×4\n'
    f'I want what you got, I say it a lot\n'
    f'I want your {words.mononoun2}, I\n'
    f'Want your {words.amphinoun2}\n'
    f'I want what you got, I say it a lot'
  )
  return lyrics

def note(word, note, duration):
  return f'<PITCH NOTE="{note}"><DURATION BEATS="{duration}">{word}</DURATION></PITCH>'

def rest(duration):
  return f'<REST BEATS="{duration}"></REST>'

def singing_xml(words):
  xml = f'''
<!DOCTYPE SINGING PUBLIC "-//SINGING//DTD SINGING mark up//EN"
"Singing.v0_1.dtd">
<SINGING BPM="112">
{rest(10.15)}
{note("I", 'B4', 0.5)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(get_syllables(words.trocheenoun1)[0], 'B4', 1.0)}
{note(get_syllables(words.trocheenoun1)[1], 'E4', 1.0)}
{rest(1.0)}
{note("I", 'B4', 1.0)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(get_syllables(words.trocheenoun2)[0], 'B4', 1.0)}
{note(get_syllables(words.trocheenoun2)[1], 'E4', 1.0)}
{rest(2.0)}
{note("I", 'A4', 1.0)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C#4', 0.5)}
{note("got", 'D4', 1.0)}
{rest(1.5)}
{note("I", 'D4', 0.5)}
{note("say", 'D4', 0.5)}
{note("it", 'C4', 0.5)}
{note("uh", 'B3', 0.5)}
{note("lot", 'A3', 1.0)}
{rest(0.5)}
{note("I", 'B4', 1.0)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(words.adj, 'B4', 1.0)}
{note(words.mononoun1, 'E4', 1.0)}
{rest(1.0)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(get_syllables(words.amphinoun1)[0], 'B4', 0.5)}
{note(get_syllables(words.amphinoun1)[1], 'B4', 1.0)}
{note(get_syllables(words.amphinoun1)[2], 'E4', 1.0)}
{rest(2.5)}
{note("I", 'A4', 0.5)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C#4', 0.5)}
{note("got", 'D4', 1.0)}
{rest(2.0)}
{note("I", 'D4', 0.5)}
{note("say", 'D4', 0.5)}
{note("it", 'C4', 0.5)}
{note("uh", 'B3', 0.5)}
{note("lot", 'A3', 1.0)}
{rest(1.0)}
<PITCH NOTE="A4"><DURATION BEATS="0.5">oh</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="0.5">my</DURATION></PITCH>
<PITCH NOTE="A4"><DURATION BEATS="1.5">god</DURATION></PITCH>
<PITCH NOTE="G4"><DURATION BEATS="0.5">oh</DURATION></PITCH>
<PITCH NOTE="G4"><DURATION BEATS="0.5">my</DURATION></PITCH>
<PITCH NOTE="G4"><DURATION BEATS="1.5">god</DURATION></PITCH>
<PITCH NOTE="D4"><DURATION BEATS="0.5">oh</DURATION></PITCH>
<PITCH NOTE="D4"><DURATION BEATS="0.5">my</DURATION></PITCH>
<PITCH NOTE="D4"><DURATION BEATS="0.5">god</DURATION></PITCH>
<PITCH NOTE="D4"><DURATION BEATS="1.0">oh</DURATION></PITCH>
<PITCH NOTE="F4"><DURATION BEATS="0.5">my</DURATION></PITCH>
<PITCH NOTE="E4"><DURATION BEATS="1.5">god</DURATION></PITCH>
{rest(1.0)}
{note("I", 'A4', 0.5)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C#4', 0.5)}
{note("got", 'D4', 1.5)}
{rest(1.0)}
{note("I", 'D4', 0.5)}
{note("say", 'D4', 0.5)}
{note("it", 'C4', 0.5)}
{note("uh", 'B3', 0.5)}
{note("lot", 'A3', 1.0)}
{rest(1.0)}
{note("I", 'B4', 0.5)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(words.mononoun2, 'B4', 1.0)}
{note("I", 'E4', 1.0)}
{rest(1.0)}
{note("want", 'B4', 0.5)}
{note("your", 'B4', 0.5)}
{note(get_syllables(words.amphinoun2)[0], 'B4', 0.5)}
{note(get_syllables(words.amphinoun2)[1], 'B4', 1.0)}
{note(get_syllables(words.amphinoun2)[2], 'E4', 0.5)}
{rest(2.0)}
{note("I", 'A4', 0.5)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C#4', 0.5)}
{note("got", 'D4', 1.5)}
{rest(1.0)}
{note("I", 'D4', 0.5)}
{note("say", 'D4', 0.5)}
{note("it", 'C4', 0.5)}
{note("uh", 'B3', 0.5)}
{note("lot", 'A3', 1.0)}
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
  lyrics = random_lyrics(word_choices)
  lyrics = lyrics if len(lyrics) <= 280 else (lyrics[:279] + '…')
  print(random_lyrics(word_choices))
  print()
  with open("xml-out.xml", "w") as xml_out:
    xml_out.write(singing_xml(word_choices))
