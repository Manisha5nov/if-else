ch=input("enter a character:")
if ch >= 'A' and ch <='Z':
    print("small letter is :",chr(ord(ch) + 32))
elif ch >='a' and ch <='z':
    print("capital letter is :",chr(ord(ch)-32))
    
