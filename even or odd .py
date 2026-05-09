a=int(input("enter the number :"))
r=a%10
if r%2==0:
    print("the number is even :",r)
a//=10
r=a%10
if r%2==0:
    print("the number is even :",r)
a//=10
if a%2==0:
    print("the number is even :",a)