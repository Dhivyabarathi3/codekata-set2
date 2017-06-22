n = int(input("enter  a starting no"))
b = int(input("enter a ending no"))
c=2
s=0
v=0
for n in range(n,b):
    for c in range(c,n):
        v = v+1
        if n%c != 0:
            s=s+1
    if s == v:
        print (n)
    c=2
    v=0
    s=0
