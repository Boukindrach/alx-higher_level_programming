#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    tuple_ = x, sentence[0]
    if x == 0:
        tuplr_ = x, None
    return tuple_
