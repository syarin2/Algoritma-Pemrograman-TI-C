def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    
    # Menghitung rata-rata nilai
    total = sum(nilai)
    jumlah_data = len(nilai)
    return total / jumlah_data

data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

print("--- Soal 1 ---")
print(f"List Nilai : {data_nilai}")
print(f"Rata-rata  : {hasil}")