#!/bin/python

import math
import os
import random
import re
import sys

def reverse_words_order_and_swap_cases(sentence):
    wlist = sentence.split()
    rlist=wlist[::-1]
    rsentence=" ".join(rlist)
    return rsentence.swapcase()
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
