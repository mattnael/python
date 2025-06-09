import numpy as np
import matplotlib.pyplot as plt

# Input data
X = [-5, -1, 0, 2]
Y = [-2, 6, 1, 2]

xs = -3.5  # Titik yang akan diinterpolasi

# Fungsi untuk menghitung koefisien polinomial
def divided_diff(X, Y):
    n = len(Y)
    a = np.zeros([n,n])
    for i in range(n):
        a[i][0] = Y[i]
    for j in range(1, n):
        for i in range(n-j):
            a[i][j] =  (a[i+1][j-1] - a[i][j-1]) / (X[i+j] - X[i])    
    return a[0] # dengan [0] menjadi baris satu saja yang muncul

# Fungsi untuk menghitung Newton Polynomial Interpolation
def newton_interp(X, Y, x):
    if x < X[0] or x > X[-1]:
        return 'NaN'
    a = divided_diff(X, Y)
    n = len(a)
    y = a[0]
    for i in range(1, n):
        yi = a[i]
        for j in range(i):
            yi *= x - X[j]
        y += yi
    return y 

# Fungsi untuk menggambaran hasil dalam grafis
def draw(X, Y, x, y):
    plt.figure(figsize=(4,3))
    plt.plot(X, Y, 'bo', label='original')
    plt.plot(x,y, 'ro', label='interpolation')
    plt.grid()
    plt.legend()
    plt.show()


yn = newton_interp(X, Y, xs)
print(yn) 
draw(X, Y, xs, yn)   