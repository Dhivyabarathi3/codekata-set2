n = int(input("enter a no"))
m=n
a=0
b=0
c=0
sum=0
while n > 0:
    a = int(n/10)
    b = int(n%10)
    n=a
    sum=sum+(b*b*b)
if m==sum:
    print(m," is armstrong number")
else:
    print(m,"not armstrong number")

