def soal_1():
    print("=== SOAL 1: MENAMPILKAN DAFTAR BUKU ===")
    # 1. List bertingkat berisi judul buku dan denda per hari
    daftar_buku = [
        ["Algoritma", 2000],
        ["Basis Data", 2500],
        ["Struktur Data", 3000],
        ["Jaringan Komputer", 2000],
        ["Pemrograman Web", 2500]
    ]
    
    # 2. Menampilkan daftar buku menggunakan for loop dengan penomoran
    print("\nDaftar Buku yang Tersedia:")
    for idx, buku in enumerate(daftar_buku, 1):
        print(f"{idx}. {buku[0]} (Denda: Rp {buku[1]}/hari)")
        
    # 3. Meminta input nomor buku dari pengguna
    try:
        pilihan = int(input("\nMasukkan nomor buku yang dipilih: "))
        
        # 4. Validasi input menggunakan if-else
        if 1 <= pilihan <= len(daftar_buku):
            buku_terpilih = daftar_buku[pilihan - 1]
            print(f"\n[SUKSES] Anda memilih buku: '{buku_terpilih[0]}'")
            print(f"Denda keterlambatan per hari: Rp {buku_terpilih[1]}")
        else:
            print("\n[ERROR] Nomor buku tidak valid! Silakan jalankan ulang program.")
    except ValueError:
        print("\n[ERROR] Input harus berupa angka!")

# Jalankan fungsi
soal_1()