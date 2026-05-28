def jumlah_digit(n):
    # Base case: jika bilangan tinggal 1 digit
    if n < 10:
        return n
    # Recursive case: ambil digit terakhir + panggil fungsi untuk sisa digitnya
    else:
        digit_terakhir = n % 10
        sisa_digit = n // 10
        return digit_terakhir + jumlah_digit(sisa_digit)

input_bilangan = 1234
hasil_digit = jumlah_digit(input_bilangan)

print("\n--- Soal 3 ---")
print(f"Input  : {input_bilangan}")
print(f"Output : {hasil_digit}")