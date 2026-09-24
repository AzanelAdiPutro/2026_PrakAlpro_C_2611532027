# Input dari user
total_belanja_2027 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2027 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member_2027 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2027 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2027 = input_promo_2027 in ["y", "ya"]

total_diskon_persen_2027 = 0

if total_belanja_2027 > 1000000:
    total_diskon_persen_2027 += 10  # Diskon belanja besar

if is_member:
    total_diskon_persen_2027 += 5  # Diskon member

if kode_promo_valid_2027:
    total_diskon_persen_2027 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2027 = total_belanja_2027 * (total_diskon_persen_2027 / 100)
total_bayar_2027 = total_belanja_2027 - nominal_diskon_2027

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2027}% (Rp {nominal_diskon_2027:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_2027:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_2027}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid
