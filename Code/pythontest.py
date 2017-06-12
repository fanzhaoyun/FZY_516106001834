# -*- coding:utf-8 -*-

name = input()
print(name)

#t1 = tuple([1,2,3])
#t2 = tuple([4,5,6])

#t = tuple([t1,t2])

#print(t)

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!= k and j!=k:
                print(i*100+j*10+k)