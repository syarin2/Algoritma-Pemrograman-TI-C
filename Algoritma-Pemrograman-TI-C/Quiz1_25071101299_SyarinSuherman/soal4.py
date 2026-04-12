while True:
    try:
        baris = int(input("Masukkan jumlah minggu: "))
        kolom = int(input("Masukkan jumlah kategori buku: "))
        if baris <= 0 or kolom <= 0:
            print("Jumlah harus lebih dari 0!")
        else:
            break
    except ValueError:
        print("Input harus berupa angka!")

matriks = []

# Input data ke matriks
for i in range(baris):
    minggu = []
    print(f"Minggu ke-{i+1}:")
    for j in range(kolom):
        while True:
            try:
                jumlah = int(input(f"  Jumlah buku kategori {j+1}: "))
                break
            except ValueError:
                print("Masukkan angka saja!")
        minggu.append(jumlah)
    matriks.append(minggu)

# Tampilkan matriks
print("\n--- Tabel Rekap Peminjaman ---")
for r in matriks:
    print(r)

# Total per minggu (baris)
print("\nTotal per Minggu:")
for i in range(baris):
    print(f"Minggu {i+1}: {sum(matriks[i])} buku")

# Total per kategori (kolom)
print("\nTotal per Kategori:")
for j in range(kolom):
    total_kolom = sum(matriks[i][j] for i in range(baris))
    print(f"Kategori {j+1}: {total_kolom} buku")