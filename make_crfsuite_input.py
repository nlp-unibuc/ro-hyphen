# -*- encoding: utf8 -*-

import fileinput
from StringIO import StringIO


def crfsuite_feature_names(size=4, negative=False):
    indices = range(-size, 0) if negative else range(1, size + 1)
    indices = map(str, indices)
    return '\t'.join(['c[%s]=%%s' % ''.join(indices[i:(i + k + 1)])
                      for k in range(size)
                      for i in range(size - k)])

def _char_ngrams(s, size=4):
    s_len = len(s)
    ngrams = []
    for n in xrange(1, min(size + 1, s_len + 1)):
        for i in xrange(s_len - n + 1):
            ngrams.append(s[i: i + n])
    return ngrams

def crfsuite_features(word, size, left_tpl, right_tpl):
    res = StringIO()    
    for k in xrange(1, len(word)):
        left, right = word[:k], word[k:]
        left_size = min(len(left), size)
        right_size = min(len(right), size)
        print >> res, '%s\t%s' % (
            left_tpl[left_size - 1] % tuple(_char_ngrams(left[-size:], size)),
            right_tpl[right_size - 1] % tuple(_char_ngrams(right[:size], size)))
    return res.getvalue()

if __name__ == '__main__':
    N = 4  # n-gram size
    left_tpl = [crfsuite_feature_names(k, True) for k in xrange(1, N + 1)]
    right_tpl = [crfsuite_feature_names(k, True) for k in xrange(1, N + 1)]

    for word in fileinput.input(openhook=fileinput.hook_encoded("utf8")):
        print crfsuite_features(word.strip().lower(),
                                size=N,
                                left_tpl=left_tpl,
                                right_tpl=right_tpl)
