n=int(input("Enter the number:"))
square=n**2
digits=len(str(n))
divisor=10**digits
last_digits = square%divisor
if n==last_digits:
    print("automorphic")
else:
    print("not automorphic")

