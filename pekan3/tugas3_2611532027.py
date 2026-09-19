# ============================================================
# B. SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
# ============================================================

print("==================================================")
print("        SISTEM TRANSAKSI TOKO")
print("==================================================")

# ============================================================
# INPUT DATA PELANGGAN DAN TRANSAKSI
# ============================================================

nama_2027 = input("Masukkan Nama Pelanggan : ")
status_2027 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2027 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_2027 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2027 = input("Masukkan Kode Promo : ").upper()


# ============================================================
# OPERATOR PERBANDINGAN
# ============================================================

# Membandingkan total belanja dengan batas minimum
syarat_belanja_2027 = total_belanja_2027 >= 200000

# Membandingkan jumlah barang dengan batas minimum
syarat_jumlah_2027 = jumlah_barang_2027 >= 3

# Membandingkan status pelanggan
status_member_2027 = status_2027 == "member"


# ============================================================
# OPERATOR MEMBERSHIP
# ============================================================

daftar_promo_2027 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# Operator in
promo_tersedia_2027 = kode_promo_2027 in daftar_promo_2027

# Operator not in
promo_tidak_tersedia_2027 = kode_promo_2027 not in daftar_promo_2027


# ============================================================
# OPERATOR LOGIKA
# ============================================================

# Operator AND
diskon_member_2027 = status_member_2027 and syarat_belanja_2027

# Operator AND untuk promo
mendapat_promo_2027 = (
    status_member_2027
    and syarat_belanja_2027
    and syarat_jumlah_2027
    and promo_tersedia_2027
)

# Operator OR
akses_dasar_2027 = status_member_2027 or syarat_belanja_2027

# Operator NOT
bukan_member_2027 = not status_member_2027


# ============================================================
# OPERATOR ARITMATIKA
# ============================================================

# Menentukan persentase dan jumlah diskon
if diskon_member_2027:
    diskon_2027 = total_belanja_2027 * 10 / 100
else:
    diskon_2027 = 0

# Total pembayaran setelah diskon
total_pembayaran_2027 = total_belanja_2027 - diskon_2027

# Harga rata-rata barang
if jumlah_barang_2027 != 0:
    rata_rata_2027 = total_belanja_2027 / jumlah_barang_2027
else:
    rata_rata_2027 = 0

# Sisa pembagian menggunakan operator %
sisa_bagi_2027 = total_belanja_2027 % jumlah_barang_2027


# ============================================================
# OPERATOR ASSIGNMENT / PENUGASAN
# ============================================================

poin_2027 = 0

# Augmented assignment +=
poin_2027 += jumlah_barang_2027

# Augmented assignment lainnya
if diskon_member_2027:
    poin_2027 += 10

# Contoh -=
saldo_2027 = total_belanja_2027
saldo_2027 -= diskon_2027


# ============================================================
# OPERATOR IDENTITY
# ============================================================

# Dua list memiliki isi yang sama tetapi merupakan objek berbeda
objek_a_2027 = ["member"]
objek_b_2027 = ["member"]

# == membandingkan nilai/isi
nilai_sama_2027 = objek_a_2027 == objek_b_2027

# is membandingkan identitas objek
identitas_sama_2027 = objek_a_2027 is objek_b_2027

# is not membandingkan apakah objek berbeda
identitas_berbeda_2027 = objek_a_2027 is not objek_b_2027


# ============================================================
# OPERATOR BITWISE
# ============================================================

# Nilai bit:
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

kode_status_2027 = 0

# Operator OR (|) untuk menggabungkan kondisi
if status_member_2027:
    kode_status_2027 = kode_status_2027 | 1

if syarat_belanja_2027:
    kode_status_2027 = kode_status_2027 | 2

if syarat_jumlah_2027:
    kode_status_2027 = kode_status_2027 | 4

if promo_tersedia_2027:
    kode_status_2027 = kode_status_2027 | 8


# Operator AND (&) untuk memeriksa kondisi tertentu
cek_member_2027 = kode_status_2027 & 1
cek_belanja_2027 = kode_status_2027 & 2
cek_jumlah_2027 = kode_status_2027 & 4
cek_promo_2027 = kode_status_2027 & 8


# Operator XOR (^) untuk membandingkan dua kode transaksi
kode_referensi_2027 = 11
hasil_xor_2027 = kode_status_2027 ^ kode_referensi_2027


# Operator Shift
hasil_shift_2027 = kode_status_2027 << 1


# ============================================================
# HAK AKSES PELANGGAN
# ============================================================

member_access_2027 = bool(cek_member_2027)
promo_access_2027 = bool(cek_promo_2027)
free_shipping_access_2027 = (
    promo_tersedia_2027 and syarat_jumlah_2027
)


# ============================================================
# OUTPUT DATA TRANSAKSI
# ============================================================

print("\n==================================================")
print("              DATA TRANSAKSI")
print("==================================================")

print("Nama Pelanggan       :", nama_2027)
print("Status Pelanggan     :", status_2027)
print("Total Belanja        : Rp", total_belanja_2027)
print("Jumlah Barang        :", jumlah_barang_2027)
print("Kode Promo           :", kode_promo_2027)


# ============================================================
# HASIL VALIDASI
# ============================================================

print("\n==================================================")
print("              HASIL VALIDASI")
print("==================================================")

print("Belanja >= Rp200000  :", syarat_belanja_2027)
print("Jumlah Barang >= 3   :", syarat_jumlah_2027)
print("Status Member        :", status_member_2027)
print("Kode Promo Tersedia  :", promo_tersedia_2027)
print("Kode Promo Tidak Ada :", promo_tidak_tersedia_2027)
print("Mendapatkan Diskon   :", diskon_member_2027)
print("Mendapatkan Promo    :", mendapat_promo_2027)


# ============================================================
# HASIL PERHITUNGAN
# ============================================================

print("\n==================================================")
print("             HASIL PERHITUNGAN")
print("==================================================")

print("Besarnya Diskon      : Rp", diskon_2027)
print("Total Pembayaran     : Rp", total_pembayaran_2027)
print("Rata-rata Barang     : Rp", rata_rata_2027)
print("Sisa Pembagian       :", sisa_bagi_2027)
print("Jumlah Poin          :", poin_2027)


# ============================================================
# HAK AKSES PELANGGAN
# ============================================================

print("\n==================================================")
print("            HAK AKSES PELANGGAN")
print("==================================================")

print("Kode Hak Akses       :", kode_status_2027)
print("Member Access        :", member_access_2027)
print("Promo Access         :", promo_access_2027)
print("Free Shipping Access :", free_shipping_access_2027)


# ============================================================
# HASIL OPERATOR IDENTITY
# ============================================================

print("\n==================================================")
print("             OPERATOR IDENTITY")
print("==================================================")

print("Objek memiliki nilai sama     :", nilai_sama_2027)
print("Objek memiliki identitas sama :", identitas_sama_2027)
print("Objek memiliki identitas beda :", identitas_berbeda_2027)


# ============================================================
# OPERASI BITWISE
# ============================================================

print("\n==================================================")
print("              OPERASI BITWISE")
print("==================================================")

print("Kode Status Transaksi")
print("0001 = Member")
print("0010 = Belanja >= Rp200000")
print("0100 = Jumlah Barang >= 3")
print("1000 = Kode Promo Tersedia")

print("\nKode Biner   :", format(kode_status_2027, "04b"))
print("Kode Desimal :", kode_status_2027)

print("\n--- Pemeriksaan Member ---")
print(format(kode_status_2027, "04b"), "& 0001")
print("Hasil Biner   :", format(cek_member_2027, "04b"))
print("Hasil Desimal :", cek_member_2027)

print("\n--- Pemeriksaan Promo ---")
print(format(kode_status_2027, "04b"), "& 1000")
print("Hasil Biner   :", format(cek_promo_2027, "04b"))
print("Hasil Desimal :", cek_promo_2027)

print("\n--- Perbandingan Status dengan XOR ---")
print("Kode Transaksi :", format(kode_status_2027, "04b"))
print("Kode Referensi :", format(kode_referensi_2027, "04b"))
print(format(kode_status_2027, "04b"), "^",
      format(kode_referensi_2027, "04b"))
print("Hasil Biner   :", format(hasil_xor_2027, "04b"))
print("Hasil Desimal :", hasil_xor_2027)

print("\n--- Shift ---")
print(format(kode_status_2027, "04b"), "<< 1")
print("Hasil Biner   :", format(hasil_shift_2027, "b"))
print("Hasil Desimal :", hasil_shift_2027)


# ============================================================
# SELESAI
# ============================================================

print("\n==================================================")
print("                 SELESAI")
print("==================================================")