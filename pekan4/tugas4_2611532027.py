print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input Data Pengunjung
nama_2027 = input("Masukkan Nama Pengunjung        : ")
umur_2027 = int(input("Input umur anda                 : "))
sim_2027 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()
jumlah_tiket_2027 = int(input("Masukkan jumlah tiket           : "))

# If tunggal untuk validasi jumlah tiket
if jumlah_tiket_2027 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_2027 = int(input("Masukkan nomor paket (1-5) : "))

# Match-case untuk memilih wahana
match paket_2027:
    case 1:
        nama_wahana_2027 = "Wahana Safari Rimba"
        harga_satuan_2027 = 50000

    case 2:
        nama_wahana_2027 = "Wahana Arung Jeram"
        harga_satuan_2027 = 75000

    case 3:
        nama_wahana_2027 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2027 = 120000

    case 4:
        nama_wahana_2027 = "Wahana Roller Coaster Kilat"
        harga_satuan_2027 = 100000

    case 5:
        nama_wahana_2027 = "Wahana All-Access VIP"
        harga_satuan_2027 = 220000

    case _:
        print("Paket wahana tidak valid!")
        exit()

# Validasi kelayakan wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2027 == 3 and umur_2027 >= 17 and sim_2027 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

elif paket_2027 == 3 and umur_2027 >= 17 and sim_2027 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")

elif paket_2027 == 3 and umur_2027 < 17 and sim_2027 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")

elif paket_2027 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

elif umur_2027 >= 10:
    print("Status Akses: Anda memenuhi syarat umur untuk wahana.")

else:
    print("Status Akses: Anda belum cukup umur untuk wahana ini.")

# Input member dan promo
is_member_2027 = input("\nApakah Anda member? (y/t)      : ").strip().lower()
kode_promo_valid_2027 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

# Menghitung subtotal
subtotal_2027 = harga_satuan_2027 * jumlah_tiket_2027

# Multi-if terpisah untuk akumulasi diskon
total_diskon_persen_2027 = 0

if subtotal_2027 >= 200000:
    total_diskon_persen_2027 += 10

if is_member_2027 in ['y', 'ya']:
    total_diskon_persen_2027 += 5

if kode_promo_valid_2027 in ['y', 'ya']:
    total_diskon_persen_2027 += 15

if jumlah_tiket_2027 >= 5:
    total_diskon_persen_2027 += 5

# Menghitung diskon dan total bayar
nominal_diskon_2027 = subtotal_2027 * (total_diskon_persen_2027 / 100)
total_bayar_2027 = subtotal_2027 - nominal_diskon_2027

# Audit transaksi
print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung   : {nama_2027}")
print(f"Wahana            : {nama_wahana_2027}")
print(f"Harga Satuan      : Rp {harga_satuan_2027:,.0f}")
print(f"Jumlah Tiket      : {jumlah_tiket_2027}")
print(f"Subtotal Belanja  : Rp {subtotal_2027:,.0f}")
print(f"Total Diskon      : {total_diskon_persen_2027}% "
      f"(Rp {nominal_diskon_2027:,.0f})")
print(f"Total Bayar       : Rp {total_bayar_2027:,.0f}")

# If-else untuk bonus
if total_bayar_2027 > 300000:
    print("Catatan Layanan   : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan   : Terima kasih telah berkunjung.")

print("\nProgram Selesai")