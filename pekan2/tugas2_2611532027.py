# ===== VARIABEL GLOBAL =====
nama_2027 = "..."
kelamin_2027 = '-'
umur_2027 = 0
skor_2027 = 0.0
batas_minimum_2027 = 75.0
lulus_2027= False
token_2027 = 6767 + 3j
alamat_2027 = """
Perumahan indah permai,
Jl. Dr.muhammad hatta no 1,
Kec. Padang Timur
Kota padang """



def main():
    print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
    bagian1()
    print("\n=== DATA PRAKTIKAN & HASIL PEMERIKASAAN ===")
    bagian2()
    print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
    bagian3()


def bagian1():
    
    global nama_2027
    global kelamin_2027
    global umur_2027
    global skor_2027
    nama_2027 = input("Masukkan Nama Mahasiswa     : ")
    kelamin_2027 = input("Masukkan Jenis Kelamin (L/P): ")
    umur_2027 = int(input("Masukkan Umur               : "))
    skor_2027 = float(input("Masukkan Skor Tes Awal      : "))



def bagian2():
    print("Nama Mahasiswa :", nama_2027, "| Tipe: ", type(nama_2027))
    print("Jenis Kelamin  :", kelamin_2027, "| Tipe: ", type(kelamin_2027))
    print("Alamat Domisili:", alamat_2027, "| Tipe: ", type(alamat_2027))
    print("Umur           :", umur_2027, "tahun | Tipe: ", type(umur_2027))
    print("Skor Tes Awal  :", skor_2027, "| Tipe: ", type(skor_2027))
    print("ID Token Sinyal:", token_2027, "| Tipe: ", type(token_2027))



def bagian3():
    
    global lulus_2027
    print("Batas Minimum Nilai:",batas_minimum_2027)
    lulus_2027 = skor_2027 >= batas_minimum_2027
    print("Apakah Dinyatakan Lulus?:", lulus_2027, "| Tipe: ", type(lulus_2027)) 

main()