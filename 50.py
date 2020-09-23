def checkprime(i):
    a = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0: a += 1
    if a == 1:return True
text=[2]
for i in range(3,46000,2):
    if checkprime(i):text.append(i)
k=len(text)
for i in range(546,22,-1):
    if i%2==0:
        x=sum(text[0:i])
        if checkprime(x):
            print(x)
            break
    else:
        z=0
        for j in range(0,k-i+1):
            x=sum(text[j:j+i])
            if x>=1000000:break
            else:
                if checkprime(x):
                    z=1
                    print(x)
                    break
        if z==1:break


#997651

