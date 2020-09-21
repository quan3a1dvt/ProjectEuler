text=[0]*1001
for i in range(1,293):
    for j in range(i+1,585):
        c=(i**2+j**2)**0.5
        if c==int(c):
            a=int(i+j+c)
            if a<=1000:text[a]+=1
print(text.index(max(text)))