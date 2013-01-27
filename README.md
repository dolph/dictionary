List of the Most Common English Words
=====================================

According to an article entitled [The words in the mental cupboard] published
by the BBC, "An ordinary person, one who has not been to university say, would
know about 35,000 quite easily."

The Unix dictionary contains far too many ridiculous words that even Google has
trouble explaining, such as `zuurveldt`, `cholecystenterorrhaphy` and `nonly`:

    $ cat /usr/share/dict/words | wc -l
    235886

Even the `enable1.txt` dictionary used by [Words with Friends](r) contains
more words than any English speaking adult would reasonably be familiar with:

    $ cat enable1.txt | wc -l
    172819

The included dictionary file, `popular.txt`, is then compiled from
[Wiktionary's word frequency lists], which are based on over 29 million words
from English TV and movie scripts.

[The words in the mental cupboard]: http://news.bbc.co.uk/2/hi/uk_news/magazine/8013859.stm
[Words with Friends]: http://www.wordswithfriends.com/
[Wiktionary's word frequency lists]: http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists#English
