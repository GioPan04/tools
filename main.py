import sys
from tabulate import tabulate as tbl

num = int(sys.argv[1])
div = int(sys.argv[2])

def convert(num, div):
    nums = []
    rests = []
    quozs = []
    nums.append("NUMERO")
    rests.append("RESTO")
    quozs.append("QUOZIENTE")
    nums.append(num)
    quoz = num
    rests.append(quoz % div)
    result = []
    result.append([num, num // div, quoz % div])
    while quoz != 1:
        quoz = quoz // div
        resto = quoz % div
        quozs.append(quoz)
        nums.append(quoz)
        rests.append(resto)
        result.append([quoz, quoz, resto])
    print(tbl(result, headers=["NUMERO", "QUOZIENTE", "RESTO"]))

convert(num, div)
