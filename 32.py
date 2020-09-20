A=[]
for i in range(10,90):
    if str(i)[0]!=str(i)[1] and str(i)[1]!="0": A.append(i)
B=[2,3,4,5,6,7,8]
C=[]
for i in range(101,898) :
    if str(i)[0]!=str(i)[1]:
        if str(i)[2] not in [str(i)[1],str(i)[0]]:
            if "0" not in [str(i)[1],str(i)[0],str(i)[2]] : C.append(i)
D=[]
def check(i):
    if str(i)[0] not in [str(i)[1],str(i)[2],str(i)[3]]:
        if str(i)[1] not in [str(i)[2], str(i)[0], str(i)[3]]:
            if str(i)[2] not in [str(i)[1], str(i)[0], str(i)[3]]:
                if str(i)[3] not in [str(i)[1], str(i)[2], str(i)[0]]:
                    if "0" not in [str(i)[1], str(i)[2], str(i)[0],str(i)[3]]:return True
for i in range(1000,5000):
    if check(i):D.append(i)
E=[]
for i in B:
    for j in D :
        if str(i) not in str(j):
            tich = i*j
            n=0
            if tich<9999:
                for k in str(tich):
                    if k in str(i) or k in str(j): n=1
                if n==0 :
                    if check(tich) and tich not in E:E.append(tich)
for i in A:
    for j in C:
        if str(i)[0] not in str(j):
            if str(i)[1] not in str(j):
                tich = i*j
                n=0
                if tich<9999:
                    for k in str(tich):
                        if k in str(i) or k in str(j): n=1
                    if n==0 :
                        if check(tich) and tich not in E:E.append(tich)

print(sum(E))




