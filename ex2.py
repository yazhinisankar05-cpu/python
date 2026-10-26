a=int(input("enter a num1:"))
b=int(input("enter a num2:"))
count = 0
for i in range(a,b+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
                print(i)
                count += 1
print("total:",count)    

    


