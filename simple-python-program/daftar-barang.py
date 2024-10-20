import time
daftar = {}

while True:
    print(f'''
====[✓]==============================[✓]====
    
    [1] Tambahkan Barang, Harga, Jumlah
    [2] Kurangi Barang
    [3] Tampilkan List Lengkap
    [4] Keluar
    
====[✓]==============================[✓]====''')
    
    user = int(input("Pilih 1/2/3/4: "))
    
    if user == 1:
        nama = input("Masukkan Nama Barang: ")
        harga = int(input("Harga per-unit: "))
        jumlah = int(input("Jumlah Barang: "))
        daftar[nama] = {"Jumlah": jumlah, "Harga": harga}
        print(f'''
        Nama     : {nama}
        Harga    : {harga}
        Jumlah   : {jumlah}''')
        print(f'''
        Total Harga Keseluruhan: {harga * jumlah}''')

    elif user == 2:
        nama = input("Nama Barang: ")
        kurang = int(input("Jumlah: "))
        if nama in daftar:
            if daftar[nama]["Jumlah"] >= kurang:
                daftar[nama]["Jumlah"] -= kurang
                print(f"Jumlah {nama} berkurang {kurang}. Sisa jumlah: {daftar[nama]['Jumlah']}")
            else:
                print(f"Jumlah {nama} tidak cukup untuk dikurangi.")
        else:
            print(f"{nama} tidak ditemukan dalam daftar.")
    
    elif user == 3:
        print("List Barang:")
        for nama_barang, info in daftar.items():
            print(f"Nama: {nama_barang}, Harga: {info['Harga']}, Jumlah: {info['Jumlah']}")

    elif user == 4:
        print("Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")