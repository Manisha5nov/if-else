a=int(input("enter the number :"))
r=a%10
s=0
s+=r
a//=10
r=a%10
s+=r
a//=10
s+=a
print("sum of three digit number is :",s)