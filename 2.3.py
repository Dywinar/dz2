chislo1 = int(input("Введите число: "))
chislo2 = int(input("Введите число: "))
if  1<= chislo1 <= 8 and  1<= chislo2 <= 8:
    if (chislo2+ chislo1) % 2 == 0 and (chislo1 != 5 and chislo2 != 5):
        print("YES")
    elif chislo1 == 5 and chislo2 == 5 :
        print("NO")
    else:
        print("NO")
else:
    print("Число должно быть в диапозоне от 1 до 8")
