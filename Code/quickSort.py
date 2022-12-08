import numpy as np
import time

# Fungsi untuk menemukan posisi partisi
def partition(array, low, high):
    # pilih elemen paling kanan sebagai pivot
    pivot = array[high]

    # pointer untuk elemen yang lebih besar
    i = low - 1

    # Traverse ke seluruh elemen
    # bandingkan setiap elemen dengan pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # Jika elemen lebih kecil maka pivot ditemukan, kemudian
            # tukar dengan elemen yang lebih besar yang ditunjukkan oleh i
            i = i + 1

            # Tukar elemen di i dengan elemen di j
            (array[i], array[j]) = (array[j], array[i])

    # Tukar elemen pivot dengan
    # elemen yang lebih besar yang ditentukan oleh i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return posisi dari partisi yang dilakukan
    return i + 1


# Fungsi untuk melakukan quicksort
def quickSort(array, low, high):
    if low < high:
        # elemen yang lebih kecil dari pivot berada di kiri
        # elemen yang lebih besar dari pivot berada di kanan
        pi = partition(array, low, high)

        # Pemanggilan rekursif ke kiri dari pivot
        quickSort(array, low, pi - 1)

        # Pembanggilan rekursif ke kanan dari pivot
        quickSort(array, pi + 1, high)


# Driver code
start_time = time.time()

# Ukuran array sesuai dengan inputan user
arraySize = input("Please enter array size: ")

# Generate angka random dalam array dengan ukuran n menggunakan numpy
numbers = np.arange(int(arraySize))
np.random.shuffle(numbers)
# print("Generated list of size " + str(arraySize) + " is:" + str(numbers))
quickSort(numbers, 0, len(numbers) - 1)

print("\n\n Execution Time --- %s seconds ---" % (time.time() - start_time))

