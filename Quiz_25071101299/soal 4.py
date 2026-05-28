def soal_4():
    print("\n=== SOAL 4: REKAP PEMINJAMAN MENGGUNAKAN MATRIKS ===")
    
    # 1. Menentukan dimensi matriks melalui user input
    try:
        jumlah_minggu = int(input("Masukkan jumlah minggu (baris): "))
        jumlah_kategori = int(input("Masukkan jumlah kategori buku (kolom): "))
        
        matriks = []
        
        # 2. Nested for loop untuk melakukan input data ke dalam matriks
        print("\n--- Input Data Peminjaman Buku ---")
        for i in range(jumlah_minggu):
            baris_minggu = []
            for j in range(jumlah_kategori):
                data_buku = int(input(f"Minggu ke-{i+1}, Kategori ke-{j+1} - Jumlah buku: "))
                baris_minggu.append(data_buku)
            matriks.append(baris_minggu)
            
        # 3. Tampilkan matriks dalam format tabel rapi
        print("\n--- Tabel Data Peminjaman ---")
        # Header Kolom Kategori
        header = "          " + "".join([f"Kat_{j+1}  " for j in range(jumlah_kategori)])
        print(header)
        print("-" * len(header) * 2)
        
        for i in range(jumlah_minggu):
            print(f"Minggu {i+1} : ", end="")
            for j in range(jumlah_kategori):
                print(f"{matriks[i][j]:<7}", end="")
            print()
            
        # 4. Menghitung total peminjaman per minggu (Baris)
        print("\nTotal Peminjaman Per Minggu:")
        for i in range(jumlah_minggu):
            total_per_minggu = sum(matriks[i])
            print(f"- Minggu ke-{i+1}: {total_per_minggu} buku")
            
        # 4. Menghitung total peminjaman per kategori (Kolom)
        print("\nTotal Peminjaman Per Kategori:")
        for j in range(jumlah_kategori):
            total_per_kategori = 0
            for i in range(jumlah_minggu):
                total_per_kategori += matriks[i][j]
            print(f"- Kategori ke-{j+1}: {total_per_kategori} buku")
            
    except ValueError:
        print("[ERROR] Input dimensi atau data harus berupa angka integer!")

soal_4()