n = int(input("enter  a no"))
if n == 1:
    print("prime no")
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
           print("is not a prime number")
           break
    else:
        print("is a prime number")
else:
   print("is not a prime number")
