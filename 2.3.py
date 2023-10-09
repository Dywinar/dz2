chislo1 = int(input("Введите число: "))
chislo2 = int(input("Введите число: "))
if (chislo2+ chislo1) % 2 == 0 and (chislo1 != 5 and chislo2 != 5) :
    print("YES")
elif chislo1 == 5 and chislo2 == 5 :
    print(""NO)
else:
    print("NO")
