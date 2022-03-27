from collections import defaultdict
from enum import Enum, auto
import random
from syllabifications import get_syllables
import uuid
import subprocess
import os

from dotenv import load_dotenv
import tweepy

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', 
  level=logging.INFO,
  datefmt='%Y-%m-%d %H:%M:%S')

class PartsOfSpeech(Enum):
  NOUN = auto()
  ADJECTIVE = auto()

class RealWordChoices:
  def __init__(self):
      self.mononoun1, self.mononoun2 = "waist", "car"
      self.trocheenoun1, self.trocheenoun2 = "suntan", "boyfriend"
      self.amphinoun1, self.amphinoun2 = "vacation", "apartment"
      self.adj = "small"


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
{note("I", 'C4', 0.5)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(get_syllables(words.trocheenoun1)[0], 'C4', 1.0)}
{note(get_syllables(words.trocheenoun1)[1], 'G3', 1.0)}
{rest(1.0)}
{note("I", 'C4', 1.0)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(get_syllables(words.trocheenoun2)[0], 'C4', 1.0)}
{note(get_syllables(words.trocheenoun2)[1], 'G3', 1.0)}
{rest(2.0)}
{note("I", 'E4', 1.0)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C4', 0.5)}
{note("got", 'D4', 1.0)}
{rest(1.5)}
{note("I", 'D4', 0.5)}
{note("say", 'D4', 0.5)}
{note("it", 'C4', 0.5)}
{note("uh", 'B3', 0.5)}
{note("lot", 'A3', 1.0)}
{rest(0.5)}
{note("I", 'C4', 1.0)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(words.adj, 'C4', 1.0)}
{note(words.mononoun1, 'G3', 1.0)}
{rest(1.0)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(get_syllables(words.amphinoun1)[0], 'C4', 0.5)}
{note(get_syllables(words.amphinoun1)[1], 'C4', 1.0)}
{note(get_syllables(words.amphinoun1)[2], 'G3', 1.0)}
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
{note("oh", 'G4', 0.5)}
{note("my", 'G4', 0.5)}
{note("god", 'G4', 1.5)}

{note("oh", 'F4', 0.5)}
{note("my", 'F4', 0.5)}
{note("god", 'F4', 1.5)}

{note("oh", 'C4', 0.5)}
{note("my", 'C4', 0.5)}
{note("god", 'C4', 0.5)}

{note("oh", 'C4', 1.0)}
{note("my", 'Eb4', 0.5)}
{note("god", 'D4', 1.5)}
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
{note("I", 'C4', 0.5)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(words.mononoun2, 'C4', 1.0)}
{note("I", 'G3', 1.0)}
{rest(1.0)}
{note("want", 'C4', 0.5)}
{note("your", 'C4', 0.5)}
{note(get_syllables(words.amphinoun2)[0], 'C4', 0.5)}
{note(get_syllables(words.amphinoun2)[1], 'C4', 1.0)}
{note(get_syllables(words.amphinoun2)[2], 'G3', 1.5)}
{rest(2.0)}
{note("I", 'E4', 0.5)}
{note("want", 'E4', 0.5)}
{note("what", 'D4', 0.5)}
{note("you", 'C4', 0.5)}
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

def clamp_length(message, length=280, suffix='…'):
  suffix_length = len(suffix)
  return (message[:length-suffix_length-1] + suffix) if len(message) > length else message

if __name__ == "__main__":
  logging.info("Loading wordlists")
  wordlists = defaultdict(list, {
    (PartsOfSpeech.NOUN, 1): file_to_list("./wordlists/NN-1.txt"),
    (PartsOfSpeech.NOUN, 2): file_to_list("./wordlists/NN-2.txt"),
    (PartsOfSpeech.NOUN, 3): file_to_list("./wordlists/NN-3.txt"),
    (PartsOfSpeech.ADJECTIVE, 1): file_to_list("./wordlists/JJ-1.txt"),
  } )

  logging.info("Choosing words")
  word_choices = WordChoices(wordlists)
  # word_choices = RealWordChoices()
  logging.info("Word choices: %s", word_choices)
  lyrics = clamp_length(random_lyrics(word_choices))

  logging.info("Lyrics: %s", lyrics)
  filename = uuid.uuid4()

  logging.info("Filename: %s", filename)
  
  logging.info("Writing XML")
  with open(f"tmp/{filename}.xml", "w") as xml_out:
    xml_out.write(singing_xml(word_choices))

  logging.info("Starting subprocess")
  subprocess.call(["./make-wwyb.sh", str(filename)])
  load_dotenv()

  CONSUMER_KEY = os.getenv("CONSUMER_KEY")
  CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
  ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
  ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuth1UserHandler(
   CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
  )  
  api = tweepy.API(auth)

  logging.info("Uploading media")
  media = api.media_upload(f"./tmp/{filename}.mp4", media_category="tweet_video")
  
  logging.info("Updating status")
  api.update_status(lyrics, media_ids=[media.media_id_string])

  logging.info("Done!")