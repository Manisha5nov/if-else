a=int(input("enter the number :"))
n=a
r=a%10
s=r**3
a//=10
r=a%10
s+=r**3
a//=10
s+=a**3
if s==n:
    print("the number is armstrong number :")
else:
    print("the number is not armstrong number :")