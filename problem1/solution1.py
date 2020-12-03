import pathlib

path = pathlib.Path(__file__).parent.absolute().__str__() + r'\\input'
f = open(path)
l = list(f)
f.close()

l = list(map(int,l))
l.sort()

#Part 1
for i in range(0,len(l)):
    for j in range(len(l)-1,i,-1): 
        k = l[i] + l[j]  
        if not k>2020:
            if k==2020:
                print(l[i]*l[j])

#Part 2
i = 0
j = 1
k = len(l) - 1
while i < j and j < k:
    while j < k:
        m = l[i]+l[j]+l[k]
        if m==2020:
            print(l[i]*l[j]*l[k])
            j = j + 1
        elif m > 2020:
            k = k - 1
        else:
            j = j + 1
    i = i + 1
    j = i + 1
    k = len(l) - 1
