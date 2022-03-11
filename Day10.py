#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    remainder = []
    
    while n > 0:
        rm = n % 2
        n = n//2
        remainder.append(rm)
    
    counter,result = 0,0
    
    for i in range(0,len(remainder)):
        if remainder[i] == 0:
            counter = 0
        else:
            counter +=1
            result = max(result,counter)
    
    print(result)
