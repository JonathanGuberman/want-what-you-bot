# Want What You Bot

In 2015, [Martin O'Leary](https://mewo2.com/) wrote [Botston](https://twitter.com/botston). From [his page](https://mewo2.com/bots/botston/) on the project:

> In June 2015 I had the [Gaston](https://www.youtube.com/watch?v=VuJTqmpBnI0) song from Disney's Beauty and the Beast stuck in my head for about a week. To exorcise it, I made this bot, which generates random versions of the chorus.

Like most of his work, it is incredible; a true thing of internet beauty. I've loved it since I first saw it.

In 2022, I had [Want What You Got](https://www.youtube.com/watch?v=gggDVJfvhgM) by [The Beaches](https://www.thebeachesband.com/) stuck in my head. To exorcise it, I made this bot. (As of yet, the exorcism hasn't worked.)

## Tech details.

Generating the lyrics is relatively easy; it just needs to fill in the blanks using words with the right part of speech, the right number of syllables, and the right stress pattern. It's generating those lists of words that's a little tricky.

I used a few parts of the [Natural Language Toolkit (NLTK)](https://www.nltk.org/): the [Carnegie Mellon Pronouncing Dictionary](https://www.nltk.org/api/nltk.corpus.reader.cmudict.html#module-nltk.corpus.reader.cmudict) module to find words' syllables and stress pattern and the [WordNet](https://www.nltk.org/api/nltk.corpus.reader.wordnet.html#module-nltk.corpus.reader.wordnet) module to find words' part of speech.

The full list of words from the Carnegie Mellon Pronouncing Dictionary had too many obscure entries, so I got a list of the 20,000 most common English words from [here](https://github.com/first20hours/google-10000-english) and used that as my initial word source.

After doing all this, I found that Martin O'Leary has already done a much better job of curating this data, _and_ he's made it [publicly available](https://github.com/mewo2/syllpos). 🤦 He also wrote the amazing [`pronouncing`](https://github.com/mewo2/pronouncingpy) library for Python. The latest version uses his approach, which eliminates proper nouns.

## To-do's

Next up I need to auto-generate the singing audio. Botston uses [Festival](http://festvox.org/festival/index.html), which I'll need to try to compile from source.