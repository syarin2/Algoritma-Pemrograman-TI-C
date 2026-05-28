def soal_3():
    print("\n=== SOAL 3: PERHITUNGAN DENDA KETERLAMBATAN ===")
    
    # Simulasi data keranjang dari buku yang dipinjam (diambil dari studi kasus)
    # Format: [Nama Buku, Tarif Denda Per Hari]
    buku_dipinjam = [["Algoritma", 2000], ["Struktur Data", 3000]]
    
    # 1 & 2. Meminta input hari keterlambatan dengan validasi while loop (harus >= 0)
    while True:
        try:
            hari_terlambat = int(input("Masukkan jumlah hari keterlambatan pengembalian: "))
            if hari_terlambat >= 0:
                break
            else:
                print("[ERROR] Hari keterlambatan tidak boleh kurang dari 0! Coba lagi.\n")
        except ValueError:
            print("[ERROR] Input harus berupa angka integers!\n")
            
    # 3. Hitung total denda berdasarkan seluruh buku yang dipinjam
    total_denda = 0
    for buku in buku_dipinjam:
        total_denda += buku[1] * hari_terlambat
        
    # Menggunakan Kondisional If-Else untuk menampilkan pesan sesuai ketentuan
    if hari_terlambat == 0:
        print("\n🎉 Tidak ada denda. Terima kasih telah mengembalikan tepat waktu!")
    else:
        print(f"\nTotal denda Anda: Rp {total_denda} (Terlambat {hari_terlambat} hari)")

# Jalankan fungsi
soal_3()
