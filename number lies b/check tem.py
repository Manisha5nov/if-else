tem=int(input("enter current temperature: "))
if tem>40:
    print("It is hot outside")
elif tem<30 and tem>=15:
    print("It is warm outside")
elif tem<15 and tem>=-50:
    print("It is cool outside")
