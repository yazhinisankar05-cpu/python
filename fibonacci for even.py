n=int(input("Enter a value:"))
a=0
b=1
for i in range(n):
    if a%2==0:
        print(a,end="")
    c=a+b
    a=b
    b=c