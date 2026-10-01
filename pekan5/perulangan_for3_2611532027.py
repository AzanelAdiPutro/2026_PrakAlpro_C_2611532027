ulang_2027 = int(input("Masukkan jumlah perulangan: "))

jumlah_2027 = 0
for i in range(1, ulang_2027 + 1):
    print(i, end=" ")
    jumlah_2027 = jumlah_2027 + i

    if i < ulang_2027:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2027, end="")
print()
print("Jumlah =", jumlah_2027)