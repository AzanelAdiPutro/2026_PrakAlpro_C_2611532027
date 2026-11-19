# Name: <AZANEL ADI PUTRO>
# NIM: <2611532027>
# Question 6

nama = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")

nama = nama.strip().lower()

posisi = nama.find(" ")

if posisi == -1:
    first_name = nama
else:
    first_name = nama[:posisi]

username = first_name + nim[-3:]

print("Username kampus:", username)

