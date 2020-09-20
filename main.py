
def isPrime(num): return all(num%d for d in range(3,int(num**0.5)+1,2))

prime, nextprime, winners =[2,3,5,7], [], []

while prime :
    for p in prime:
        for q in [1,3,7,9]:
            if isPrime(10*p+q) : nextprime.append(10*p+q)
    prime ,nextprime = nextprime, []
    for p in prime:
        if all([isPrime(int(str(p)[i:])) for i in range(1,len(str(p)))]) : winners.append(p)

print(sum([p for p in winners if p%10 !=1]))