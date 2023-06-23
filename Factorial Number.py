def fact(n):
    if n==0 or n==1:
        return 1
    res=1
    while n>0:
        res=res*n
        n-=1
    return res
n=int(input())
print(fact(n))

Output
5
120
