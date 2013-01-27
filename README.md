List of the Most Common English Words
=====================================

According to an article entitled [The words in the mental cupboard] published
by the BBC, "An ordinary person, one who has not been to university say, would
know about 35,000 quite easily."

The Unix dictionary contains far too many ridiculous words that even Google has
trouble explaining, such as `zuurveldt`, `cholecystenterorrhaphy` and `nonly`:

    $ cat /usr/share/dict/words | wc -l
    235886

Even `enable1.txt`, the more verbose version of the *Official Scrabble Player's
Dictionary* (`ospd.txt`) (which is limited to words of 8 letters or less) used
by [Words with Friends](r), contains more words than any English speaking adult
would reasonably be familiar with:

    $ cat enable1.txt | wc -l
    172819

`popular.txt`
-------------

`popular.txt` represents the common subset of words found in both `enable1.txt`
and [Wiktionary's word frequency lists], which are in turn compiled by
statistically analyzing a sample of 29 million words used in English TV and
movie scripts.

    $ cat popular.txt | wc -l
    25322

These are 25,322 words that everyone should be familiar with.

[The words in the mental cupboard]: http://news.bbc.co.uk/2/hi/uk_news/magazine/8013859.stm
[Words with Friends]: http://www.wordswithfriends.com/
[Wiktionary's word frequency lists]: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#English
