from hashids import Hashids
import sys

if sys.argv[1] == None:
    salt = input("Salt: ")
else:
    salt = sys.argv[1]

hashids = Hashids(salt=salt, min_length=10)
var = input("ID or Code: ")
try:
    id = int(var)
    print(hashids.encode(id))
except ValueError as err:
    print(hashids.decode(var))