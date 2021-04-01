import re
def val(a):
    if a=='A':
        return 1
    elif a=='B':
        return 2
    else :
        return 3
def sum(s):
    sum=0
    for i in range(len(s)):
        if s[i-1] in ['A','B','C']:
            if i > len(s)-1 :
                sum+=val(s[i-1])
            elif s[i] in ['2','3','4','5','6','7','8','9']:
                sum+=val(s[i-1]) * int(s[i])
                i+=1
            else:
                sum+=val(s[i-1])
    return sum
str=input()
x=str.replace ( "(" , ')' )
y=x.split(")")
ans=0
for i in range (len(y)):
    ans+=sum(y[i-1])
print(ans)
