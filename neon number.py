n=int(input("enter a number:"))
square=n**2
sum=0
while square>0:
    last_digits=square%10
    sum=sum+last_digits
    square=square//10
if sum==n:
     print("neon number")
else:
  print("not neon number")
