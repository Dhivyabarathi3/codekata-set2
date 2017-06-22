n =  int(input("enter a starting no"))
m = int(input("enter a  ending no"))
c=0
for n in range(n,m):
    a=n
    while n>0:
        r=int(n%10)
        n=int(n/10)
        c=c+r*r*r
    if a==c:
        print(c)
    c=0
