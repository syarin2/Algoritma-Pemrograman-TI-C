DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"]
# ==== BAGIAN A ====

riwayat = []

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer:
        return "seri"
    if (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
       (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
       (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "pemain"
    else:
        return "komputer"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
        pilihan_pemain = input("Masukkan pilihan (gunting/batu/kertas): ").strip().lower()
        if pilihan_pemain in ["gunting", "batu", "kertas"]:
            break
        print("Pilihan tidak valid! Masukkan gunting, batu, atau kertas.")
    print(f"Pilihan komputer: {pilihan_komputer}")
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)

    if hasil == "pemain":
        print("Hasil: Anda menang!")
    elif hasil == "komputer":
        print("Hasil: Komputer menang!")
    else:
        print("Hasil: Seri!")

    return hasil

def main_satu_ronde(nama, nomor_ronde):
    nomor_giliran = 0
    menang_pemain = 0
    menang_komputer = 0
    while menang_pemain < 3 and menang_komputer < 3:
        hasil_giliran = main_satu_giliran(nomor_giliran)
        nomor_giliran += 1
        if hasil_giliran == "pemain":
            menang_pemain
        elif hasil_giliran == "komputer":
            menang_komputer += 1
        nomor_giliran += 1

        score = menang_pemain
    return [nama, score]

# ==== BAGIAN B ====
def tampilkan_riwayat(riwayat):
    if not riwayat:
        print("Belum ada riwayat.")
        return

    print("\n=== RIWAYAT PERMAINAN ===")
    print("No\tNama\t\tSkor")
    for i, data in enumerate(riwayat, start=1):
        nama, skor = data
        print(f"{i}\t{nama}\t\t{skor}")

def bubble_sort_riwayat(riwayat):
    salinan = riwayat[:]  # buat salinan
    n = len(salinan)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salinan[j][1] < salinan[j + 1][1]:
                salinan[j], salinan[j + 1] = salinan[j + 1], salinan[j]
    return salinan

def tampilkan_leaderboard(riwayat):
    if not riwayat:
        print("Belum ada riwayat, leaderboard kosong.")
        return

    terurut = bubble_sort_riwayat(riwayat)
    print("\n=== LEADERBOARD ===")
    print("Peringkat\tNama\t\tSkor")
    for i, data in enumerate(terurut, start=1):
        nama, skor = data
        tanda = "*" if i == 1 else ""
        print(f"{i}{tanda}\t\t{nama}\t\t{skor}")

# ==== BAGIAN C ====
# ==== PROGRAM UTAMA ====
if __name__ == "__main__":
    nama_pemain = input("Masukkan nama Anda: ").strip()
    if nama_pemain == "":
        nama_pemain = "Pemain"

    riwayat = []
    nomor_ronde = 1

    while True:
        hasil_ronde = main_satu_ronde(nama_pemain, nomor_ronde)
        riwayat.append(hasil_ronde)

        lanjut = input("\nMain lagi? (y/n): ").strip().lower()
        if lanjut != "ya":
            break
        nomor_ronde += 1

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)

