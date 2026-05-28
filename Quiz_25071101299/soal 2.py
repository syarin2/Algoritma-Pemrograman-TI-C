def soal_2():
    print("\n=== SOAL 2: MENGHITUNG TOTAL PEMINJAMAN ===")
    daftar_buku = [
        ["Algoritma", 2000],
        ["Basis Data", 2500],
        ["Struktur Data", 3000],
        ["Jaringan Komputer", 2000],
        ["Pemrograman Web", 2500]
    ]
    
    keranjang_pinjam = []
    
    # 1. While loop untuk terus menambah buku sampai input 0
    while True:
        print("\nDaftar Buku:")
        for idx, buku in enumerate(daftar_buku, 1):
            print(f"{idx}. {buku[0]}")
        print("0. Selesai dan Hitung")
        
        try:
            pilihan = int(input("Pilih nomor buku yang ingin dipinjam: "))
            
            if pilihan == 0:
                break
            elif 1 <= pilihan <= len(daftar_buku):
                buku_terpilih = daftar_buku[pilihan - 1]
                hari = int(input(f"Berapa hari rencana meminjam buku '{buku_terpilih[0]}'? "))
                
                # 2. Menyimpan judul, denda asli, dan lama pinjam ke keranjang
                keranjang_pinjam.append([buku_terpilih[0], buku_terpilih[1], hari])
                print(f"💥 '{buku_terpilih[0]}' ditambahkan ke daftar pinjam.")
            else:
                print("[ERROR] Pilihan tidak tersedia!")
        except ValueError:
            print("[ERROR] Masukkan input angka yang valid!")
            
    # 3. Menampilkan daftar buku yang dipinjam menggunakan for loop
    if keranjang_pinjam:
        print("\n--- Ringkasan Buku yang Dipinjam ---")
        total_estimasi_denda = 0
        for idx, item in enumerate(keranjang_pinjam, 1):
            print(f"{idx}. Judul: {item[0]} | Durasi Pinjam: {item[2]} Hari")
            # 4. Hitung simulasi jika terlambat 1 hari dari jadwal
            total_estimasi_denda += item[1]
            
        print(f"\nTotal estimasi denda jika seluruh buku terlambat 1 hari: Rp {total_estimasi_denda}")
    else:
        print("\nTidak ada buku yang dipinjam.")

# Jalankan fungsi
soal_2()