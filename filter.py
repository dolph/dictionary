"""
Filters two input dictionaries, eliminating duplicate words and returning the
common subset.
"""
import argparse


def get_words(filename):
    try:
        fp = open(filename, 'r')
        words = fp.readlines()
    finally:
        fp.close()

    return set(word.strip() for word in words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument('dictionaries', metavar='<dictionary>', nargs=2,
                        help='path to word list file')
    args = parser.parse_args()

    first = get_words(args.dictionaries[0])
    second = get_words(args.dictionaries[1])

    for word in sorted(first.intersection(second)):
        print word
