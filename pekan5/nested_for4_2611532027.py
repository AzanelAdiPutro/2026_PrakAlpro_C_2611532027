tinggi_2027 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2027 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2027 = tinggi_2027
    c_2027 = a_2027
    lebar_2027 = (2 * tinggi_2027) - 2

    for i_2027 in range(1, tinggi_2027 + 1):
        b_2027 = c_2027 + 1
        for j_2027 in range(1, lebar_2027 + 1):
            if i_2027 == 1 or i_2027 == tinggi_2027:
                print("#" if j_2027 == 1 or j_2027 == lebar_2027 else "=", end="")
            else:
                if j_2027 == 1 or j_2027 == lebar_2027:
                    print("|", end="")
                else:
                    if j_2027 == c_2027:
                        print("<", end="")
                    elif j_2027 == b_2027:
                        print(">", end="")
                    elif j_2027 == (lebar_2027 - c_2027):
                        print(">", end="")
                    elif j_2027 == (lebar_2027 - c_2027 + 1):
                        print("<", end="")
                    elif j_2027 > b_2027 and j_2027 < (lebar_2027 - c_2027):
                        print("-", end="")
                    else:
                        print(" ", end="")

        print()
        a_2027 -= 2
        c_2027 = (-a_2027) + 2 if a_2027 <= 0 else a_2027
