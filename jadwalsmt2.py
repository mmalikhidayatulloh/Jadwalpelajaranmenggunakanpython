print("JADWAL KULIAH SEMESTER 2".center(50, ":"))
print("PERHATIKAN !\nsenin\t= 1\nselasa\t= 2\nrabu\t= 3\nkamis\t= 4\njum'at\t= 5\nsabtu\t= 6\nminggu\t= 7")
hari_ini = int(input("hari ini: "))
senin = "07:30-09:00\tPraktikum Fisika Dasar II\n12:10-13:50\tFisika Dasar II\n15:50-17:30\tFisika Matematika I"
selasa = "09:50-11:30\tTermodinamika\n14:00-15:40\tGelombang"
rabu = "09:30-11:30\tFisika Matematika I\n14:00-15:40\tFisika Dasar II\n17:40-20:30\tAbsen Praktikum Fisika Dasar II"
kamis = "09:50-11:30\tKimia Dasar\n12:10-13:50\tTermodinamika\n15:50-17:30\tPerbaikan Fisika Dasar I"
jumat = "09:20-11:00\tBiologi\n13.00-14.40\tPerbaikan Fisika Dasar I\n15:40-18:30\tAbsen Praktikum Kimia Dasar"
sabtu = "LIBUR !!!".upper()
minggu = "LIBUR !!!".upper()
if hari_ini == 1:
    print("SENIN".center(40, "="))
    print(senin)
    print("=".center(41, "="))
elif hari_ini == 2:
    print("SELASA".center(40, "="))
    print(selasa)
    print("=".center(41, "="))
elif hari_ini == 3:
    print("RABU".center(40, "="))
    print(rabu)
    print("=".center(41, "="))
elif hari_ini == 4:
    print("KAMIS".center(40, "="))
    print(kamis)
    print("=".center(41, "="))
elif hari_ini == 5:
    print("JUM\'AT".center(40, "="))
    print(jumat)
    print("=".center(41, "="))
elif hari_ini == 6:
    print("SABTU".center(40, "="))
    print(sabtu)
    print("=".center(41, "="))
elif hari_ini == 7:
    print("MINGGU".center(40, "="))
    print(minggu)
    print("=".center(41, "="))
else:
    print("Masukkan angka yang benar!")
