def Fibinocci_Series(n): 
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(n-2):
           c=a+b
           print(c,end=" ")
           a=b
           b=c
n=int(input())
Fibinocci_series(n)

Output
5
0 1 1 2 3 
