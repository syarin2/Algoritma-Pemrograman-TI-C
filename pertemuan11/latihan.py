# ================= DATA =================
data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38,
        505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44,
        421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84,
        155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303,
        16, 25, 321]

# ================= RADIX SORT =================
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# ================= MERGE SORT =================
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ================= SEARCH =================
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]
    return -1, None

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, None

# ================= MAIN PROGRAM =================
print("Data sebelum sorting:")
print(data)

# Radix Sort
radix_data = data.copy()
radix_sort(radix_data)
print("\nHasil Radix Sort:")
print(radix_data)

# Merge Sort
merge_data = data.copy()
merge_sort(merge_data)
print("\nHasil Merge Sort:")
print(merge_data)

# Input user
target = int(input("\nMasukkan angka yang ingin dicari: "))

# Linear Search (pakai data asli)
index_lin, value_lin = linear_search(data, target)
if index_lin != -1:
    print(f"\nLinear Search: ditemukan di index {index_lin}, nilai = {value_lin}")
else:
    print("\nLinear Search: tidak ada")

# Binary Search (pakai data yang sudah di-sort)
index_bin, value_bin = binary_search(merge_data, target)
if index_bin != -1:
    print(f"Binary Search: ditemukan di index {index_bin}, nilai = {value_bin}")
else:
    print("Binary Search: tidak ada")