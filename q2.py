import math
def sieve(n,a):
   
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
          
        if (prime[p] == True):
              
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1):
        if prime[p]:
            a.append(p)

a=[]
result=[]
i=1
sieve(70,a)
found=True
while(found):
    found =False
    i+=2
    j=0
    while(i>=a[j]):
        if math.sqrt(i-a[j])*math.sqrt(i-a[j])==i-a[j] :
            result.append((i,a[j],i-a[j]))
            found=True
            break
        j+=1
        if j>len(a):
            break
    if found==False:
        print(i)
        break
print(result)