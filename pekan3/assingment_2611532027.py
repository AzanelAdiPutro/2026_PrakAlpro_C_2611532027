angka1_2027 = int(input("input angka-1: "))
angka2_2027 = int(input("input angka-2: "))

print("nilai awal angka-1 : ", angka1_2027)
print("nilai awal angka-2 : ", angka2_2027)

hasil = angka1_2027
print("\nAsignment biasa")
print("hasil = ", hasil)

hasil += angka2_2027
print("\nAssignment penjumlahan (+=)")
print("Hasil =", hasil)

hasil -= angka2_2027
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)


hasil = angka1_2027
hasil *= angka2_2027
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

if angka2_2027 != 0:
    hasil = angka1_2027
    hasil /= angka2_2027
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    
    hasil = angka1_2027
    hasil //= angka2_2027
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    
    hasil = angka1_2027
    hasil %= angka2_2027
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

hasil = angka1_2027
hasil **= angka2_2027
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)


