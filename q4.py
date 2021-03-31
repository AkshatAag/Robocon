def rev_no(a):
    rev = 0
 
    while(a > 0):
        n = a % 10
        rev = rev * 10 + n
        a = a // 10
    return rev      



t=int(input())
while t :
    x, y = [int(x) for x in input().split()]  
    
    print(rev_no(rev_no(x)+y))
    t-=1
    