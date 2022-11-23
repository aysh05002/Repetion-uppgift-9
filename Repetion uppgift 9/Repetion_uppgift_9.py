from random import randint

print("Du ska svara pa tio multiplikation fragor\n")
for i in range(10):
    x=randint(1,9)
    y=randint(1,9)
    z=x*y
    print("Vad ar",x,"*",y,"?")
    v=int(input("Svar: "))
    if z==v:
        print("Svar ar ratt\n")
    else:
        print("Svar ar fel\n")

print("Klart\n")