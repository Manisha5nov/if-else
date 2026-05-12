a=int(input("Enter  First number: "))
b=int(input("Enter second number: "))
c=int(input("Enter Third number: "))
if (a<b and c<a):
    print(f"{b} is greatest and {c} is smallest")
elif(b<a and c<b):
    print(f"{a} is greatest and {c} is smallest ")
elif(a<c and b<a):
    print(f"{c} is greatest and {b} is smallest")
elif(b<c and a<b):
    print(f"{c} is greatest and {a} is smallest")
elif(c<b and a<c):
    print(f"{b} is greatest and {a} is smallest ")
elif(b<a and c<b):
    print(f"{a} is greatest and {c} is smallest")
elif (a==b and b!=c):
    print(f"{a} and {b} are equal and {c} is smallest")  
elif (a==c and c!=b):
    print(f"{a} and {c} are equal and {b} is smallest")
elif (b==c and c!=a):
    print(f"{b} and {c} are equal and {a} is smallest")
elif (a==b and b==c):
    print("All three numbers are equal")    