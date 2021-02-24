def fak(x):
    if x == 0:
        return 1
    return x * fak(x - 1)


x = int(input("Bir değer girin:"))
print("sonuc:", fak(x))