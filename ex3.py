a=input("enter:")
for i in a:
    print(i)
####


a=input("enter:")
count = 0
for i in a:
    print(i)
    count += 1
print("total length:",count)
####

a=input("Enter a string:")
count=0
for i in a:
    if i in"a,e,i,o,u":
        count += 1
print("no of vowels:",count)
