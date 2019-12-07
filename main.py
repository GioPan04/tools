import sys
num = int(sys.argv[1])
div = int(sys.argv[2])

def convert(num, div):
    nums = []
    rests = []
    quozs = []
    nums.append(num)
    quoz = num
    rests.append(quoz % div)
    while quoz != 1:
        quoz = quoz // div
        resto = quoz % div
        quozs.append(quoz)
        nums.append(quoz)
        rests.append(resto)
    print(nums)
    print(quozs)
    print(rests)

convert(num, div)
