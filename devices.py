import random

devices = ['Android', 'iOS', 'Web', 'macOS', 'Linux', 'Windows']
res = []

for x in range(1,10):
    random.shuffle(devices)
    res.extend(devices)

output = ""

for dev in res:
    output += dev + ', '

print(output)