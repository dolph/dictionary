List of the Most Common English Words
=====================================

According to an article entitled [The words in the mental cupboard] published
by the BBC, "An ordinary person, one who has not been to university say, would
know about 35,000 quite easily."

The Unix dictionary (included here as `unix-words`) contains far too many
ridiculous words that even Google has trouble explaining, such as `zuurveldt`,
`cholecystenterorrhaphy` and `nonly`:

    $ cat unix-words | wc -l
    235886

Even `enable1.txt`, the more verbose alternative to the *Official Scrabble
Players Dictionary* (`ospd.txt`, which is limited to words of 8 letters or
less) used by [Words with Friends], contains more words than any English
speaking adult would reasonably be familiar with:

    $ cat enable1.txt | wc -l
    172823

`popular.txt`
-------------

`popular.txt` represents the common subset of words found in both `enable1.txt`
and [Wiktionary's word frequency lists], which are in turn compiled by
statistically analyzing a sample of 29 million words used in English TV and
movie scripts.

    $ cat popular.txt | wc -l
    25322

These are 25,322 words that everyone should be familiar with.

Files
-----

* `popular.txt`: the list of common words described above.
* `enable1.txt`: the ENABLE word list.
* `ospd.txt`: the *Official Scrabble Players Dictionary* word list.
* `unix-words`: a copy of the Unix dictionary, `/usr/share/dict/words`.
* `filter.py`: prints the words that two word lists have in common, which is
  how `popular.txt` was produced:

      $ python3 filter.py enable1.txt <wiktionary-word-list> > popular.txt

[The words in the mental cupboard]: https://news.bbc.co.uk/2/hi/uk_news/magazine/8013859.stm
[Words with Friends]: https://www.wordswithfriends.com/
[Wiktionary's word frequency lists]: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#English
