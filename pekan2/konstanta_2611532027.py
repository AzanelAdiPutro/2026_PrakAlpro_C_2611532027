from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2027 = float(input("Masukkan nilai jari-jari: "))
luas_2027 = PI * jari_2027 * jari_2027
print("Luas lingkaran dengan jari-jari %.2f adalah: %.2f" % (jari_2027, luas_2027))