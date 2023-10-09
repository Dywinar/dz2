chislo1 = int(input("Введите число: "))
chislo2 = int(input("Введите число: "))
if 1<= chislo1 <= 8 and 1<= chislo2 <= 8:
    if (chislo1 + chislo2) % 2 == 0:
        print("NO")
    else:
        print("YES")
else:
print("Ввели не коретное число")
