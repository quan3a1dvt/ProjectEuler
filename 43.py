import itertools
result=[]
result.extend([''.join(i for i in j) for j in itertools.permutations('1234567890',10)])
A=[17,13,11,7,5,3,2]
sums=0
for i in result:
    if all(int(i[(7-n):(10-n)])%A[n]==0 for n in range(0,7)):sums+=int(i)
print(sums)
