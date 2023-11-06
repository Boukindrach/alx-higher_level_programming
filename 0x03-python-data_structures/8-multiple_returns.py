#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        tuplr_ = x, None
    else:
        tuple_ = x, sentence[0]
    return tuple_
