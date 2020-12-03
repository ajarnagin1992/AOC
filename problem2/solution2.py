import pathlib
import re

path = pathlib.Path(__file__).parent.absolute().__str__() + r'\\input'
f = open(path)
l = list(f)
f.close()

#Part 1
validcounter = 0
for i in range(len(l)):
    l[i] = list(re.split(r"[\-:\s]+",l[i]))
    x,y,rule,password,junk = l[i] #Can't figure out why preceeding regex split leaves an empty string in the resulting list, using junk var as hacky workaround
    x = int(x)
    y = int(y)
    
    result = re.findall("{}".format(rule),password)
    if len(result) >= x and len(result) <= y:
        validcounter += 1

print(validcounter)

#Part 2
validcounter = 0
for i in range(len(l)):
    x,y,rule,password,junk = l[i] #Can't figure out why preceeding regex split leaves an empty string in the resulting list, using junk var as hacky workaround
    x = int(x) - 1
    y = int(y) - 1
    if (password[x] == rule) != (password[y] == rule):
        validcounter += 1

print(validcounter)

