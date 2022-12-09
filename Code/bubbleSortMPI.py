# Import library yang diperlukan
from mpi4py import MPI
import numpy as np
import time
from operator import itemgetter

# Assign variabel Message Parsing Interface
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank() # Mengembalikan nilai rank dari prosess didalam communicator

# Algoritma Bubble Sort
def bubbleSort(numArrays):
    # Set Variabel swapped dengan nilai true
    swapped = True
    # Jika swapped masih bernilai true lakukan perulangan
    while swapped:
        swapped = False
        for i in range(len(numArrays) - 1):
            if numArrays[i] > numArrays[i + 1]:
                # Swap the elements
                numArrays[i], numArrays[i + 1] = numArrays[i + 1], numArrays[i]
                # Set the flag to True so we'll loop again
                swapped = True

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if rank == 0:
    arraySize = input("Masukkan Ukuran array: ")

    # Generate angka random dalam array dengan ukuran n
    numbers = np.arange(int(arraySize))
    np.random.shuffle(numbers)
    print("Generated list of size " + str(arraySize) + " is: " + str(numbers))

    chunks = np.array_split(numbers, size)
else:
    chunks = None

# Memulai script dengan proses paralel
start_time = time.time()

chunk = comm.scatter(chunks, root=0)
print("Process " + str(rank) + " has this chunk of data: " + str(chunk))

# panggil fungsi bubbleSort
# bubbleSort(chunk)
insertionSort(chunk)


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



    print("\n\n Sorted Array: " + str(sortedArray))

    # End of script
    executionTime = (time.time() - start_time)
    print("\n\n Waktu Eksekusi --- %s second ---" % executionTime)