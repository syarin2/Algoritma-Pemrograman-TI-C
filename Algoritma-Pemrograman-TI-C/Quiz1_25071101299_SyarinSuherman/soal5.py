class Buku:
    def __init__(self, judul, denda_per_hari):
        self.judul = judul
        self.denda_per_hari = denda_per_hari
    
    def tampilkan(self):
        print(f"{self.judul} - Denda Rp{self.denda_per_hari}/hari")

class Peminjaman:
    def __init__(self):
        self.total_denda = 0
    
    def tambah(self, buku, hari_terlambat):
        self.total_denda += buku.denda_per_hari * hari_terlambat
    
    def ringkasan(self):
        print(f"Total denda yang harus dibayar: Rp{self.total_denda}")

# Program Utama
buku1 = Buku("Algoritma", 2000)
buku2 = Buku("Basis Data", 2500)
buku3 = Buku("Sistem Operasi", 1500)

katalog = [buku1, buku2, buku3]

print("--- Katalog Buku (OOP) ---")
for i, b in enumerate(katalog):
    print(f"{i+1}. ", end="")
    b.tampilkan()

# Transaksi
transaksi = Peminjaman()
pilih = int(input("\nPilih nomor buku: ")) - 1
telat = int(input("Masukkan hari keterlambatan: "))

transaksi.tambah(katalog[pilih], telat)
transaksi.ringkasan()