a = int(input("Enter a number"))
b = int(input("Enter a 2nd number"))
c = int(input("Enter a 3rd number"))
if a>b:
    print("a is greater")
    if c>a:
        print("c is greater")
    else b>c:
        print("b is greater")
        print("c is greater")
else:
    print("c is greater")
