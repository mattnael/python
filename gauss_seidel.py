import numpy as np
import math as mt

aug = np.array([
    [8, 3, -3, 14],
    [-2, -8, 5, 5],
    [3, 5, 10, -8]
])

eps = 1e-2  # Epsilon

# Fungsi untuk mengubah matriks menjadi absolut
def absolut(mat):
    n = len(mat)
    mat = mat.copy()  # Hindari perubahan langsung pada matriks asli
    for i in range(n):
        for j in range(n):
            if mat[i][j] < 0:
                mat[i][j] *= -1
    return mat  

# Fungsi untuk mengecek diagonal dominance
def dominant(mat):
    n = len(mat)
    arr = absolut(mat[:, :-1])  # Abaikan kolom augmented saat pengecekan
    dom = True
    for i in range(n):
        total = sum(arr[i]) - arr[i][i]  # Total baris tanpa elemen diagonal
        if arr[i][i] <= total:
            dom = False
            break  # Keluar lebih cepat jika tidak memenuhi syarat
    return dom 

# Fungsi untuk menghitung variabel per iterasi
def var_calc(mat, x):
    n = len(x)
    new_x = x.copy()  # Salin x agar perubahan tidak mempengaruhi iterasi
    for i in range(n):
        a = 0
        for j in range(n):
            if j != i:
                a += mat[i][j] * x[j]  
        new_x[i] = (mat[i][-1] - a) / mat[i][i]  
    return new_x  

#fungsi untuk menghitung error iterasi
def iter_arr(x, x_o):
   e_i = 0
   n = len(x)
   for i in range(n):
       e_i += (x[i] - x_o [i]) ** 2
   e_i = mt.sqrt(e_i)
   return e_i     

#fungsi untuk menjalankan gauss seidel
def gauss_seidel(mat, et):
    n = len(mat)
    e_i = 9999
    if dominant (mat[:]) == False:
        return None
    x = np.zeros(n)
    # alternatif x = np.zeros(n) -> x = [i for i in range[n]]
    
    x_old = x.copy()
    while e_i > et:
        x =  var_calc(mat, x)
        e_i = iter_arr(x, x_old)
        x_old = x.copy()
    return x    

    
result = gauss_seidel(aug,eps)
if result is None:
    print("SPL tidak dapat diselesaikan")
else:
    print("Solusi: " + str(result))       


