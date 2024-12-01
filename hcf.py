a = int(input("enter a number"))
b = int(input("enter a number"))
while b:
    x = b
    b = a%b
    a = x
print(a)