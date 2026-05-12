a=int(input("Enter  First number: "))
b=int(input("Enter second number: "))
c=int(input("Enter Third number: "))
if (a>b and a>c):
    print(f"{a} is greatest")
    if (b<c):
        print(f"{b} is smallest")
    elif (c<b):
        print(f"{c} is smallest")
elif (b>a and b>c):
    print(f"{b} is greatest")
    if (a<c):
        print(f"{a} is smallest")
    elif (c<a):
        print(f"{c} is smallest")
elif (c>a and c>b):
    print(f"{c} is greatest")
    if (a<b):
        print(f"{a} is smallest")
    elif (b<a):
        print(f"{b} is smallest")
elif (a==b and b!=c):
    print(f"{a} and {b} are equal and {c} is smallest")
elif (a==c and c!=b):
    print(f"{a} and {c} are equal and {b} is smallest")
elif (b==c and c!=a):
    print(f"{b} and {c} are equal and {a} is smallest")
elif (a==b and b==c):
    print("All three numbers are equal") 
elif (a==b and b>c):
    print(f"{a} and {b} are equal and {c} is smallest")
elif (a==c and c>b):
    print(f"{a} and {c} are equal and {b} is smallest")
elif (b==c and c>a):
    print(f"{b} and {c} are equal and {a} is smallest")
elif (a==b and b<c):
    print(f"{a} and {b} are equal and {c} is greatest")     
elif (a==c and c<b):
    print(f"{a} and {c} are equal and {b} is greatest")
elif (b==c and c<a):
    print(f"{b} and {c} are equal and {a} is greatest")
