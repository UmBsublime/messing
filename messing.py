#!/usr/bin/env python


l = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(l)):

    if i >= 8:
        d=5-i
    else:
        d=5
    print l[i:i+d]



from collections import deque

t = deque(l,10)

for i in range(len(t)):
    print ('{}. {}'.format(i, list(t)[:5]))
    t.rotate(-1)
print list(t)
t.rotate()
print t