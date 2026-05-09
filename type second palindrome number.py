a=int(input("emter the number :"))
n=a
b=a%10
a//=10
c=a%10
a//=10
if b==a:
    print("the number is palindrome number :",n)
else:
    print("the number is not paindrome number :",n)