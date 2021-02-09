print("JADWAL KULIAH SEMESTER 1".center(50, ":"))
print("PERHATIKAN !\nsenin\t= 1\nselasa\t= 2\nrabu\t= 3\nkamis\t= 4\njum'at\t= 5\nsabtu\t= 6\nminggu\t= 7")
hari_ini = int(input("hari ini: "))
senin = "06:30-07:15\tOLAHRAGA\n07:25-09:05\tFISIKA DASAR\n14:45-16:30\tMETODE PENGUKURAN  FISIS"
selasa = "11:00-12:00\tKALKULUS DAN VEKTOR\n13:00-14:45\tBAHASA INDONESIA"
rabu = "07:10-09:10\tfisika dasar 1\n14:45-16:30\tpraktikum fisika dasar 1".upper()
kamis = "09:10-10:55\tpendidikan agama islam\n11:00-13:30\tkalkulus dan vektor\n15:25-16:00\tpendidikan pancasila dan kewarganegaraan".upper()
jumat = "07:10-08:50\tbahasa inggris\n14.45-16.00\tinternet of things".upper()
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