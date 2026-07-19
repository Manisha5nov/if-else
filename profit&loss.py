c_p=int(input("enter a c_p ="))
s_p=int(input("enter a s_p ="))
if s_p>c_p:
    print("profit =",s_p-c_p)
elif s_p<c_p:
    print("loss =",c_p-s_p)
else:
    print("not profit and not loss")