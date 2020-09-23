import itertools
def check(n):
    n.sort()
    for i in range(0,len(n)-2):
        for j in range(i+1,len(n)-1):
            k=2*n[j]-n[i]
            if checkprime(k)==True:
                if k in n:print(str(n[i])+str(n[j])+str(k))
result=[]
A=[-1]*9999
def checkprime(i):
    a = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0: a += 1
    if a == 1:return True

for i in range(1001,9998,2):
    if checkprime(i):
        result.append(i)
for i in result:
    text = []
    for x in [''.join(y for y in z) for z in itertools.permutations(str(i), 4)]:
        if checkprime(int(x)):text.append(int(x))
    text=list(set(text))
    check(text)