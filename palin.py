n=int(input("enter a no"))
rev=0
m=n
while n > 0:
    dig = int(n % 10)
    rev = rev * 10 + dig
    n = int(n / 10)
    print(rev)

if m == rev:
    print("this no is palindrome")
else:
    print("not palindrome")
