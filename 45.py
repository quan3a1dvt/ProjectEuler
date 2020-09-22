def check(n):
    a=(-1+(1+8*n)**0.5)/2
    b=(1+(1+24*n)**0.5)/6
    if a==int(a) and b==int(b):
        return True
n=144
while True:
    a=n*(2*n-1)
    if check(a): break
    n+=1
print(n*(2*n-1))


