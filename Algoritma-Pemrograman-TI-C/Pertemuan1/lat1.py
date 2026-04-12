DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

def tebak_angka(angka_rahasia, maks_percobaan):
    for i in range(maks_percobaan):
        try:
            tebakan = int(input(f"[{i+1}/{maks_percobaan}] Tebak: "))
            if tebakan == angka_rahasia:
                print("Benar!"); return True, maks_percobaan - (i + 1)
            print("Terlalu " + ("kecil" if tebakan < angka_rahasia else "besar"))
        except ValueError:
            print("Input tidak valid!")
    return False, 0

def hitung_skor(berhasil, sisa):
    return sisa * 10 if berhasil else 0

def main_satu_ronde(nama, ronde):
    rahasia = DAFTAR_ANGKA[ronde % len(DAFTAR_ANGKA)]
    print(f"\n--- Ronde {ronde + 1} ({nama}) ---")
    
    hasil, sisa = tebak_angka(rahasia, 7)
    return [nama, hitung_skor(hasil, sisa)]

# BAGIAN B — Riwayat Skor (Matrix 2D)

def tampilkan_riwayat(riwayat):
    print("\n=== RIWAYAT PERMAINAN ===")
    if len(riwayat) == 0:
        print("Belum ada riwayat.")
    else:
        # Loop manual tanpa format tabel rumit
        for i in range(len(riwayat)):
            data = riwayat[i]
            nama = data[0]
            skor = data[1]
            print(i + 1, ".", nama, "| Skor:", skor)

# BAGIAN C — Leaderboard & Selection Sort

def selection_sort_riwayat(riwayat):
    # Copy list secara manual pakai loop biar jelas
    data_urut = []
    for item in riwayat:
        data_urut.append(item)
    
    n = len(data_urut)
    for i in range(n):
        maks_idx = i
        for j in range(i + 1, n):
            # Cek skor di indeks 1
            if data_urut[j][1] > data_urut[maks_idx][1]:
                maks_idx = j
        
        # Tukar posisi cara klasik
        temp = data_urut[i]
        data_urut[i] = data_urut[maks_idx]
        data_urut[maks_idx] = temp
        
    return data_urut

def tampilkan_leaderboard(riwayat):
    print("\n=== LEADERBOARD (SKOR TERTINGGI) ===")
    if not riwayat:
        print("Belum ada data.")
        return
    
    sorted_data = selection_sort_riwayat(riwayat)
    print(f"{'Rank':<5} | {'Nama':<15} | {'Skor':<5}")
    print("-" * 30)
    
    for i in range(len(sorted_data)):
        nama = sorted_data[i][0]
        skor = sorted_data[i][1]
        rank_display = f"{i+1}*" if i == 0 else f"{i+1}"
    
        print(f"{rank_display:<5} | {nama:<15} | {skor:<5}")

def main():
    print("Selamat datang di Game!")
nama_input = input("Masukkan nama anda: ")

riwayat_game = []
ronde = 0
main_lagi = "y"

while main_lagi == "y":
    hasil_satu_ronde = main_satu_ronde(nama_input, ronde)
    riwayat_game.append(hasil_satu_ronde)
    
    ronde = ronde + 1
    main_lagi = input("\nMain lagi? (y/n): ")

tampilkan_riwayat(riwayat_game)
tampilkan_leaderboard(riwayat_game)
print("Sampai jumpa!")