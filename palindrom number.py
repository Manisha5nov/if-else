a=int(input("enter the number :"))
n=a
r=a%10
a//=10
s=0
s=100*r
r=a%10
s+=10*r
a//=10
s+=a
if s==n:
    print("the number is palindrome number :",s)
else:
    print("the number is not palindrome number :",s)