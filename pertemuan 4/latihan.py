stok_awal = 100
print("=== Sistem Manajemen Stok Toko ===")
print(f"Stok saat ini: {stok_awal} unit")

try:
    jumlah_beli = input("Masukkan jumlah barang yang dibeli: ")
    jumlah = int(jumlah_beli)
    
    # Validasi input diletakkan sebelum kalkulasi stok akhir
    if jumlah < 0:
        print("Peringatan: Jumlah beli tidak boleh angka negatif.")
    elif jumlah > stok_awal:
        print("Peringatan: Stok tidak mencukupi!")
    else:
        # Kalkulasi hanya dilakukan jika input valid
        stok_akhir = stok_awal - jumlah
        print(f"Transaksi Berhasil! Sisa stok sekarang: {stok_akhir} unit")

except ValueError:
    print("Kesalahan: Harap masukkan angka bulat (contoh: 5). Jangan masukkan huruf!")

finally:
    print("Sesi pengecekan stok selesai.")