# List buku: [Judul, Denda per hari]
daftar_buku = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["Pemrograman Web", 3000],
    ["Jaringan Komputer", 2000],
    ["Sistem Operasi", 1500]
]

print("--- Daftar Buku Tersedia ---")

# Menampilkan buku dengan penomoran
for i in range(len(daftar_buku)):
    print(f"{i+1}. {daftar_buku[i][0]} (Denda: Rp{daftar_buku[i][1]}/hari)")

# Input nomor buku
pilihan = int(input("\nPilih nomor buku (1-5): "))

# Validasi input
if 1 <= pilihan <= len(daftar_buku):
    indeks = pilihan - 1
    print(f"Anda memilih: {daftar_buku[indeks][0]}")
    print(f"Denda per hari: Rp{daftar_buku[indeks][1]}")
else:
    print("Error: Nomor buku tidak valid!")


