def bilangan_prima(n):
    daftar_prima = []
    
    # Menggunakan range dari 1 sampai n
    for i in range(1, n + 1):
        if i > 1:
            # Cek apakah i memiliki pembagi selain 1 dan dirinya sendiri
            is_prima = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prima = False
                    break
            if is_prima:
                daftar_prima.append(i)
                
    return daftar_prima

n_target = 50
hasil_prima = bilangan_prima(n_target)

print("\n--- Soal 2 ---")
print(f"Bilangan prima dari 1 sampai {n_target} adalah:")
print(hasil_prima)