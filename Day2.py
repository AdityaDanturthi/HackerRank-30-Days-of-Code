import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:  
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tipper=tip_percent/100
    taxper=tax_percent/100
    tip = meal_cost * tipper
    tax = meal_cost * taxper
    totalcost = meal_cost + tip + tax
    totalcost = round(totalcost)
    print("Total cost: ", totalcost)
    return totalcost

solve(12.00, 20, 8)
