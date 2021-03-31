from string import ascii_lowercase as abcd
n=int(input())
s=input()
str=[i for i in s.split()]
j=0
a=97
flag=True
for j in range(n//2):
    if str[j]==str[n-j-1]:
         pass
    else:
        print("false")
        flag=False
        break
if flag:
    for j in range (n//2-1):
        if str[j+1]==str[j] or str[j+1]==chr(ord(str[j])+1):
            pass
        else:
            print ("false")
            flag=False
            
if flag:
    print("true")
