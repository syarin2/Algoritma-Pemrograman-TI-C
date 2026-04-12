# daftar buku
daftar_buku = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["Pemrograman Web", 3000],
    ["Jaringan Komputer", 2000],
    ["Sistem Operasi", 1500]
]

# contoh keranjang pinjam
keranjang_pinjam = [
    ["Algoritma", 3],
    ["Basis Data", 2]
]

# input keterlambatan
while True:
    try:
        terlambat = int(input("\nMasukkan jumlah hari keterlambatan: "))
        if terlambat < 0:
            print("Error: Hari tidak boleh negatif!")
        else:
            break
    except ValueError:
        print("Input harus angka!")

# menghitung denda
denda_akhir = 0

for buku in keranjang_pinjam:
    for item in daftar_buku:
        if item[0] == buku[0]:
            denda_akhir += item[1] * terlambat

if terlambat == 0:
    print("Tidak ada denda.")
else:
    print(f"Total denda Anda: Rp{denda_akhir}")