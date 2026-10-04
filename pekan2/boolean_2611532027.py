
# deklarasi variabel dengan tipe data boolean
is_lulus_2027 = True
is_cumlaude_2027= True

# menggunakan boolean
nilai_2027 = 85
batas_lulus_2027 = 75

# menentukan nilai boolean dari kondisi
status_kelulusan_2027 = nilai_2027 >= batas_lulus_2027 # Hasilnya akan True

# mencetak nilai boolean
print("=== Check Kelulusan ===")
print("Nilai:", nilai_2027)
print("Apakah lulus?:", status_kelulusan_2027)
if is_lulus_2027 and is_cumlaude_2027:
    print("Selamat, Anda lulus dengan peringkat cumlaude!")
