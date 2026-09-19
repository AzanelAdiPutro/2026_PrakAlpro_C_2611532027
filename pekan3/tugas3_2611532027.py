# Sistem Simulasi Transaksi dan Validasi Akses Toko

print("=== SISTEM KASIR DAN VALIDASI AKSES TOKO ===")

# Input data pelanggan
nama = input("Masukkan nama pelanggan: ")
status = input("Masukkan status pelanggan (member/non-member): ").lower()

# Input transaksi
harga_barang = float(input("Masukkan harga barang: Rp "))
jumlah = int(input("Masukkan jumlah barang: "))

# Menghitung total transaksi
total = harga_barang * jumlah

print("\n=== HASIL TRANSAKSI ===")
print("Nama pelanggan :", nama)
print("Status pelanggan :", status)
print("Harga barang :", harga_barang)
print("Jumlah barang :", jumlah)
print("Total awal : Rp", total)

# Menentukan diskon
if status == "member" and total >= 100000:
    diskon = 0.10
elif status == "member":
    diskon = 0.05
else:
    diskon = 0

nilai_diskon = total * diskon
total_bayar = total - nilai_diskon

# Validasi kelayakan promo
layak_promo = (status == "member") and (total >= 150000)

# Validasi hak akses
punya_akses = (status == "member") or (total >= 200000)

# Hasil diskon
print("\n=== VALIDASI ===")

if diskon > 0:
    print("Status diskon : Mendapatkan diskon")
    print("Diskon :", diskon * 100, "%")
else:
    print("Status diskon : Tidak mendapatkan diskon")

# Hasil promo
if layak_promo:
    print("Kelayakan promo : LAYAK")
else:
    print("Kelayakan promo : TIDAK LAYAK")

# Hasil akses
if punya_akses:
    print("Hak akses promo : DIIZINKAN")
else:
    print("Hak akses promo : DITOLAK")

# Total pembayaran
print("\n=== TOTAL PEMBAYARAN ===")
print("Nilai diskon : Rp", nilai_diskon)
print("Total yang harus dibayar : Rp", total_bayar)

print("\n=== TRANSAKSI SELESAI ===")