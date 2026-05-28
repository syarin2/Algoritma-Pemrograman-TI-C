def bubble_sort_optimized(arr):
    # Menyalin data agar tidak merusak list asli
    data_copy = list(arr)
    n = len(data_copy)
    total_swap = 0
    
    for i in range(n):
        swapped = False
        # n-i-1 karena elemen terakhir di setiap iterasi sudah pasti berada di posisi yang benar
        for j in range(0, n - i - 1):
            if data_copy[j] > data_copy[j + 1]:
                # Tukar elemen
                data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
                total_swap += 1
                swapped = True
        
        # Jika tidak ada pertukaran sama sekali dalam satu putaran, artinya array sudah urut
        if not swapped:
            break
            
    return data_copy, total_swap


def selection_sort_descending(arr):
    # Menyalin data agar tidak merusak list asli
    data_copy = list(arr)
    n = len(data_copy)
    total_swap = 0
    
    for i in range(n):
        # Cari elemen terbesar di sisa list yang belum terurut
        max_idx = i
        for j in range(i + 1, n):
            if data_copy[j] > data_copy[max_idx]:
                max_idx = j
                
        # Tukar elemen terbesar yang ditemukan dengan elemen di indeks i
        if max_idx != i:
            data_copy[i], data_copy[max_idx] = data_copy[max_idx], data_copy[i]
            total_swap += 1
            
    return data_copy, total_swap

data = [
    290, 1012, 731, 801, 992, 1395, 367, 519, 795, 1385, 274, 154, 219, 1410, 83, 
    589, 553, 362, 594, 851, 173, 657, 581, 397, 543, 791, 226, 81, 1459, 126, 
    941, 491, 1207, 1093, 1473, 951, 267, 1371, 864, 953, 1119, 212, 1266, 120, 
    723, 643, 205, 130, 9, 16, 1053, 507, 1381, 1122, 1323, 758, 713, 1219, 375, 
    951, 98, 1011, 642, 1099, 1098, 453, 7, 1137, 53, 1352, 553, 380, 1324, 473, 
    519, 923, 13, 592, 10, 546, 65, 1440, 1002, 1444, 510, 1266, 901, 1444, 691, 
    650, 373, 896, 681, 916, 943, 323, 783, 1385, 891, 621, 687, 1384, 268, 211, 
    708, 1067, 736, 1223, 990, 1145, 448, 731, 486, 381, 1441, 312, 181, 785, 157, 
    793, 1029, 1273, 846, 1473, 57, 785, 588, 582, 920, 808, 644, 1182, 1101, 579, 
    623, 556, 858, 59, 163, 1236, 310, 1308, 962, 356, 1005, 883, 582, 786, 958, 321
]

hasil_bubble, swap_bubble = bubble_sort_optimized(data)
hasil_selection, swap_selection = selection_sort_descending(data)


print("Bubble Sort (kecil → besar):")
print(hasil_bubble)
print(f"Jumlah swap Bubble Sort: {swap_bubble}")
print("-" * 50)
print("Selection Sort (besar → kecil):")
print(hasil_selection)
print(f"Jumlah swap Selection Sort: {swap_selection}")