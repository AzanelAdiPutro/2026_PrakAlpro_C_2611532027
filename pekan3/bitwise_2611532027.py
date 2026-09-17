print("\n=====================================")
print("3. OPERATOR BITWISE")
print("=====================================")

angka1_2027 = int(input("Masukkan angka bitwise-1: "))
angka2_2027 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2027, "| biner =", bin(angka1_2027))
print("angka2 =", angka2_2027, "| biner =", bin(angka2_2027))

hasil = angka1_2027 & angka2_2027
print("\nBitwise AND (&)")
print(angka1_2027, "&", angka2_2027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

hasil = angka1_2027 | angka2_2027
print("\nBitwise OR (|)")
print(angka1_2027, "|", angka2_2027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

hasil = angka1_2027 ^ angka2_2027
print("\nBitwise XOR (^)")
print(angka1_2027, "^", angka2_2027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

hasil = ~angka1_2027
print("\nBitwise NOT (~)")
print("~", angka1_2027, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_2027 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_2027, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

hasil = angka1_2027 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_2027, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))