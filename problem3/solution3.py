import pathlib

path = pathlib.Path(__file__).parent.absolute().__str__() + r'\\input'
f = open(path)
l = list(f)
f.close()


def treecounter(slopeX,slopeY):
    x = 0
    y = 0
    treecounter = 0

    while y < len(l):
        if l[y][x] == '#':
            treecounter += 1
        x = (x + slopeX) % (len(l[y]) - 1)
        y += slopeY

    return(treecounter)

#Part 1
print(treecounter(3,1))

#Part 2
a = treecounter(1,1)
b = treecounter(3,1)
c = treecounter(5,1)
d = treecounter(7,1)
e = treecounter(1,2)
 
print(a*b*c*d*e)