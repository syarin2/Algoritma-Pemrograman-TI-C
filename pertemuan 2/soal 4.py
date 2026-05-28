def pangkat_rekursif(a, b):
    # Base case: angka berapapun pangkat 0 adalah 1
    if b == 0:
        return 1
    # Base case: angka berapapun pangkat 1 adalah angka itu sendiri
    elif b == 1:
        return a
    # Recursive case: a^b = a * a^(b-1)
    else:
        return a * pangkat_rekursif(a, b - 1)

angka_base = 2
angka_pangkat = 5
hasil_pangkat = pangkat_rekursif(angka_base, angka_pangkat)

print("\n--- Soal 4 ---")
print(f"Input  : a = {angka_base}, b = {angka_pangkat}")
print(f"Output : {hasil_pangkat}")