import itertools

b=[1,2,3,4,5,6,7]
def checkprime(n):
    k=0
    for i in range(1,int(n**0.5)+1,2):
        if n%i==0:k+=1
    if k==1:return True
max=0
result=[]
result.extend([int(''.join(j for j in i)) for i in itertools.permutations('1234567', 7)])
for i in result:
    if i%2==1:
        if checkprime(i):
            if i>max:max=i
print(max)

