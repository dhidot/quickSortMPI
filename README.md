# Tugas Besar Mata Kuliah Komputasi Tersebar dan Parallel 

1. Chandra Nugrahanindhito - 24060120140098
2. Nurida Larasati - 24060120120005
3. Mumtaz Hana Najda Hafidh - 24060120130107

## Description
Project ini merupakan project yang mengimplementasikan Message Passing Interface (MPI) dalam melakukan sorting atau pengurutan. Pada Project ini akan dibandingkan antara algoritma quik sort menggunakam MPI dengan algoritma quick sort secara sekuensial

## How to install MPI on windows OS machine
1. Install Miscrosoft MPI (https://www.microsoft.com/en-us/download/details.aspx?id=57467)
2. Add the path 
```
C:\Program Files\Microsoft MPI\bin
```
  to your system variabel

## How to install mpi4py
1. on command line / terminal 
```
pip install mpi4py
```

## How to execute mpi4py project 
```
mpiexec -n [num of process] python [file name] 
```

```
mpiexec -n 5 python quickSortMPI.py
```
