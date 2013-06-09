ro-hyphen
=========

End of line hyphenation and syllabication in Romanian.

**Authors**: Liviu P. Dinu, Vlad Niculae (@vene), Octavia-Maria Șulea

**License**: BSD 3-clause

Usage
-----

    echo "dinozaur \n telefon" | python make_crfsuite_input.py | crfsuite tag -m models/4grams.C=1.0.nb.model

    1
    0
    1
    0
    1
    0
    1

    1
    0
    1
    0
    1
    2

Tags are as described in the paper and are different between the two available
models.  With the `nb` model, tags represent the distance since the last
syllable split, and therefore the `0` tag translates to a hyphen.
With the simple model, `1` translates to a hyphen.

The output above should be read as: *di-no-za-ur*, *te-le-fon*.
If you need to use diacritics, please use a UTF-8 encoded file instead
of standard input, to avoid terminal encoding issues.
