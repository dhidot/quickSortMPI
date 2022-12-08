# Import library yang diperlukan
from mpi4py import MPI
import numpy as np
import time
from operator import itemgetter

# Assing variabel untuk komunikasi antar proses
comm = MPI.COMM_WORLD # Mendefinisikan komunikasi antar proses
size = comm.Get_size() # Mendapatkan jumlah proses
rank = comm.Get_rank() # Mengembalikan nilai rank dari prosess didalam communicator

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

if rank == 0:
    arraySize = input("Masukkan Ukuran array: ")

    # Generate angka random dalam array dengan ukuran n
    numbers = np.arange(int(arraySize))
    np.random.shuffle(numbers)
    # print("Generated list of size " + str(arraySize) + " is: " + str(numbers))

    chunks = np.array_split(numbers, size)
else:
    chunks = None

# Memulai script dengan proses paralel
start_time = time.time()

# scatter data ke semua proses
chunk = comm.scatter(chunks, root=0)
# print("Process " + str(rank) + " has this chunk of data: " + str(chunk))

# panggil fungsi quickSort
quickSort(chunk, 0, len(chunk) - 1)

# gather data dari semua proses
sortedArrays = comm.gather(chunk, root=0)

if rank == 0:
    iteratorNumbers = np.zeros((len(sortedArrays),), dtype=int)
    sortedArray = []
    for my_index in range(0, int(arraySize)):
        iterator = [
            (i, (99999999 if iteratorNumbers[i] >= len(sortedArrays[i]) else sortedArrays[i][iteratorNumbers[i]])) for i
            in range(0, len(sortedArrays))]
        res = min(iterator, key=itemgetter(1))
        iteratorNumbers[res[0]] = iteratorNumbers[res[0]] + 1
        sortedArray.append(res[1])
        iterator = []

    # End of script
    executionTime = (time.time() - start_time)
    print("\n\n Waktu Eksekusi --- %s second ---" % executionTime)