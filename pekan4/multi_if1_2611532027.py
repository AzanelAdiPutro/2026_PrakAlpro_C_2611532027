umur_2027 = int(input("Input umur anda: "))
sim_2027 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2027 >= 17 and sim_2027 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2027 >= 17 and sim_2027!= 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2027 < 17 and sim_2027 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_2027 < 17 and sim_2027!= 'y':
    print("Anda Belum Cukup Umur bawa motor")