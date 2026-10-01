ulang_2027 = int(input("Masukkan nilai batas: "))

jumlah_2027 = 0
for i in range(1, ulang_2027 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2027 = jumlah_2027 + i

        if i < ulang_2027-1:
            print(" + ", end="")
        else:
            print(" = ", jumlah_2027, end="")
print()
print("Jumlah =", jumlah_2027)