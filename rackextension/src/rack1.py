import rack
from rack import main
# query = input()
import sys
# print (sys.argv)
# print (sys.argv[2:])
stringquery=' '.join(sys.argv[2:])
print(stringquery)
# print("hello")
# query = "send email"

main.main(stringquery)
# /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py