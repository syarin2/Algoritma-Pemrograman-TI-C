# DATA STRUKTUR FOLDER
struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

# TUGAS A - TOTAL UKURAN
def total_ukuran(folder: dict) -> int:
    total = 0
    for item in folder.values():
        if isinstance(item, dict):
            total += total_ukuran(item)
        else:
            total += item
    return total

# TUGAS B - JUMLAH FILE
def hitung_file(folder: dict) -> int:
    jumlah = 0
    for item in folder.values():
        if isinstance(item, dict):
            jumlah += hitung_file(item)
        else:
            jumlah += 1
    return jumlah

# TUGAS C - FILE TERBESAR
def cari_terbesar(folder: dict) -> tuple:
    nama_terbesar = ""
    ukuran_terbesar = 0

    for nama, item in folder.items():
        if isinstance(item, dict):
            nama_file, ukuran = cari_terbesar(item)
            if ukuran > ukuran_terbesar:
                nama_terbesar = nama_file
                ukuran_terbesar = ukuran
        else:
            if item > ukuran_terbesar:
                nama_terbesar = nama
                ukuran_terbesar = item

    return (nama_terbesar, ukuran_terbesar)

# TUGAS D - TAMPILKAN TREE
def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "  " * level
    print(f"{indent}📁 {nama}")

    for nama_item, item in folder.items():
        if isinstance(item, dict):
            tampilkan_tree(item, nama_item, level + 1)
        else:
            print(f"{'  ' * (level + 1)}📄 {nama_item} ({item} KB)")

# MAIN PROGRAM (OUTPUT)
print("Total ukuran skripsi:", total_ukuran(struktur), "KB")
print("Jumlah file:", hitung_file(struktur), "file")

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")

print("\nStruktur Folder:")
tampilkan_tree(struktur["Skripsi_Aqil"], "Skripsi_Aqil")