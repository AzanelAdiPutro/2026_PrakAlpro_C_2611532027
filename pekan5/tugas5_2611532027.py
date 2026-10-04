print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_2027 = int(input("Masukkan ukuran skala jam pasir (N): "))

# =========================
# BORDER ATAS
# =========================
print("#", end="")

for i_2027 in range(4 * n_2027 + 5):
    print("=", end="")

print("#")


# =========================
# FASE 1: JAM PASIR ATAS
# =========================
for baris_2027 in range(n_2027, 0, -1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    spasi_2027 = 2 * (n_2027 - baris_2027)

    for i_2027 in range(spasi_2027):
        print(" ", end="")

    # Angka menurun
    for angka_2027 in range(baris_2027, 0, -1):
        print(angka_2027, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2027 in range(1, baris_2027 + 1):
        print(" ", end="")
        print(angka_2027, end="")

    # Spasi penyeimbang kanan
    for i_2027 in range(spasi_2027):
        print(" ", end="")

    print(" |")


# =========================
# FASE 2: POROS PUSAT
# =========================
print("| ", end="")

spasi_2027 = 2 * n_2027 + 1

for i_2027 in range(spasi_2027):
    print(" ", end="")

print("<*>", end="")

for i_2027 in range(spasi_2027):
    print(" ", end="")

print(" |")


# =========================
# FASE 3: JAM PASIR BAWAH
# =========================
for baris_2027 in range(1, n_2027 + 1):

    print("| ", end="")

    # Spasi penyeimbang kiri
    spasi_2027 = 2 * (n_2027 - baris_2027)

    for i_2027 in range(spasi_2027):
        print(" ", end="")

    # Angka menurun
    for angka_2027 in range(baris_2027, 0, -1):
        print(angka_2027, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2027 in range(1, baris_2027 + 1):
        print(" ", end="")
        print(angka_2027, end="")

    # Spasi penyeimbang kanan
    for i_2027 in range(spasi_2027):
        print(" ", end="")

    print(" |")


# =========================
# BORDER BAWAH
# =========================
print("#", end="")

for i_2027 in range(4 * n_2027 + 5):
    print("=", end="")

print("#")