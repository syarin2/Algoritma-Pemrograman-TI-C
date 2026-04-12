# List buku: [Judul, Denda per hari]
daftar_buku = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["Pemrograman Web", 3000],
    ["Jaringan Komputer", 2000],
    ["Sistem Operasi", 1500]
]

keranjang_pinjam = []
total_estimasi_denda = 0

print("--- Sistem Peminjaman Buku ---")

while True:
    for i in range(len(daftar_buku)):
        print(i+1, daftar_buku[i][0])
    
    pilihan = int(input("Pilih nomor buku (0 untuk selesai): "))
    
    if pilihan == 0:
        break
    elif 1 <= pilihan <= len(daftar_buku):
        hari = int(input(f"Lama pinjam buku '{daftar_buku[pilihan-1][0]}' (hari): "))
        
        # Simpan judul dan lama pinjam
        keranjang_pinjam.append([daftar_buku[pilihan-1][0], hari])
        
        # Simulasi denda jika terlambat 1 hari
        total_estimasi_denda += daftar_buku[pilihan-1][1]
    else:
        print("Nomor tidak valid, silakan coba lagi.")

print("\n--- Ringkasan Peminjaman ---")
for buku in keranjang_pinjam:
    print(f"- {buku[0]} dipinjam selama {buku[1]} hari")

print(f"Total estimasi denda (jika semua telat 1 hari): Rp{total_estimasi_denda}")