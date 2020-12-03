import pathlib
import re

path = pathlib.Path(__file__).parent.absolute().__str__() + r'\\input'
f = open(path)
l = list(f)
l = [r.rstrip('\n') for r in l]
f.close()

#Part 1
validcounter = 0
for i in range(len(l)):
    l[i] = list(re.split(r"[\-:\s]+",l[i]))
    x,y,rule,password = l[i] 
    x = int(x)
    y = int(y)
    
    result = re.findall("{}".format(rule),password)
    if len(result) >= x and len(result) <= y:
        validcounter += 1

print(validcounter)

#Part 2
validcounter = 0
for i in range(len(l)):
    x,y,rule,password,junk = l[i]
    y = int(y) - 1
    if (password[x] == rule) != (password[y] == rule):
        validcounter += 1

print(validcounter)

