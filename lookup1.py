import math

sqt_table = {}

def commute_inverse_square(n):
    result = 1 / math.sqrt(n)
    return result

def build_lookup_table():
    for i in range(0, 1000):
        sqt_table[i] = commute_inverse_square(i)

def faster_commute_square(n):
    return sqt_table[n]

build_lookup_table()
print(sqt_table)

