batas_2027 = int(input("Masukkan nilai batas: "))
for line_2027 in range(1, batas_2027 + 1):
    for j_2027 in range(1, (-1 * line_2027 + batas_2027) + 1):
        print(".", end="")
    print(line_2027)