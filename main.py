a = int(input("enter a number"))
c = a
rev = 0
while a > 0:
    digit = a%10
    rev = rev*10+digit
    a = a//10
if rev==c:
    print("its a palandrome number")
else:
    print("its not a palandrome number")