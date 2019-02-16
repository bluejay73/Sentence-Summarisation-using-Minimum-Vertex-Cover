import re
import math
import numpy as np
from itertools import chain
from collections import Counter

def jaccard():
    documents= []
    with open('doc','r') as f:
        for line in f:
            documents.append(line)
    for i in range(len(documents)):
        for j in range(len(documents)):
            a=set(documents[i])
            b=set(documents[j])
            print('%.2f' %(1.0 * len(a&b)/len(a|b))),
        print("\n")
jaccard()
