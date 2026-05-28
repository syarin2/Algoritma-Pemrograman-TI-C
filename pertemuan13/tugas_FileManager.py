# import time
import os

#1. menampilkan menu utama dengan 4 pilihan
def tampilan_menu():
    print("===============================")
    print("PYTHON FILE MANAGE v1.0")
    print("===============================")

    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

    pilihan = int(input("Pilih Menu: "))
    return pilihan

def pilih_file():
    print("File tersedia: ")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

    pilihan = int(input("Pilih Menu (nomor): "))
    return pilihan

#2. read
def read_file(file):
    print(f"--- Isi {file} ---")
    with open(file ) as f : 
        print(f.read())

#3. write
def write_file(file):
    with open(file, "a") as f :
        f.write(input(f"--- {file} ---\n"))

#4. delete
def delete_file(file):
    if os.path.exists(file):
        konfirmasi = input(f"Yakin hapus {file}? (y/n): ")

        if konfirmasi.lower() == 'y':
            os.remove(file)
            print("File berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")

    else:
        print("File tidak ada.")
        
def main():
    while True:
        pilih_menu = tampilan_menu()
        match pilih_menu:
            case 1:
                pilih_file_R = pilih_file()
                match pilih_file_R:
                    case 1:
                        read_file("Catatan.txt")
                    case 2:
                        read_file("Tugas.txt")
                    case 3:
                        read_file("Jadwal.txt")
            case 2:
                pilih_file_W = pilih_file()
                match pilih_file_W:
                    case 1:
                        write_file('Catatan.txt')
                    case 2 : 
                        write_file('Tugas.txt')
                    case 3 :
                        write_file('Jadwal.txt')
            case 3 :
                pilihan_file_D =  pilih_file()
                match pilihan_file_D : 
                    case 1 :
                        delete_file('Catatan.txt')
                    case 2 : 
                        delete_file('Tugas.txt')
                    case 3 :
                        delete_file('Jadwal.txt')
            case 0 :
                break
        print('------------------------------')

main()