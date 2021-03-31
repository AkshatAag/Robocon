s=input()
i=0
while s and i!=-1:
    i=s.find("bot")
    s=s[:i]+s[i+3: ]
if s=="": 
    print("True")
else:
    print("False")

