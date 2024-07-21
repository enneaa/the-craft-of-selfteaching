
[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0]
k=[m+n for m in 'ABC' for n in 'XYZ']
print(k)

L=['Hello','World','IBM','Apple']
s=[s.lower() for s in L]

print(s)


# -*- coding:utf-8 -*-
L1=['Hello','World','18','Apple',None]

print(L1)
L2=[s.lower() for s in L1 if isinstance(s,str)]

print(L2)