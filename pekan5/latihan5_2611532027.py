tinggi_2027 = int(input("Masukkan tinggi segitiga: "))

for i_2027 in range(1, tinggi_2027 + 1):
    # 1. cetak spasi
    for s_2027 in range(tinggi_2027 - i_2027):
        print(" ", end="")
    # 2. cetak bintang
    for b_2027 in range(i_2027):
        print("* ", end="")
    print()