def checkprime(n):
    a=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:a+=1
    if a==1:return True
    else:return False
def check(n):
    k=True
    for i in range(1,int((n//2)**0.5)+1):
        a=n-2*i*i
        if checkprime(a):
            k=False
            break
    if k :return True
    else:return False
x=15
while True:
    if not checkprime(x):
        if check(x):
            print(x)
            break
    x+=2
#5777


