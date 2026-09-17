angka1_2027 = int(input("input angka-1: "))
angka2_2027 = int(input("input angka-2: "))

hasil = angka1_2027 + angka2_2027
print("\noperator penjumlahan")
print("hasil : ", hasil)

hasil = angka1_2027 - angka2_2027
print("\noperator pengurangan")
print("hasil : ", hasil)

hasil = angka1_2027 * angka2_2027
print("\noperator perkalian")
print("hasil : ", hasil)

if angka2_2027 != 0:
	hasil = angka1_2027 / angka2_2027
	print("\noperator pembagian")
	print("hasil : ", hasil)

	hasil = angka1_2027 // angka2_2027
	print("\noperator pembagian bulat")
	print("hasil : ", hasil)

	hasil = angka1_2027 % angka2_2027
	print("\noperator sisa bagi")
	print("hasil : ", hasil)
else:
	print("angka kedua tidak boleh bernilai 0")

hasil = angka1_2027 ** angka2_2027
print("\noperator pangkat")
print("hasil : ", hasil)