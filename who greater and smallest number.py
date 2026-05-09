a=int(input("enter the number :"))
r=a%10
s=r
l=r
a//=10
r=a%10
if s>r:
    s=r
if l<r:
    l=r
a//=10
if s>a:
    s=a
if l<a:
    l=a
print("smallest number is :",s)
print("greater number is :",l)