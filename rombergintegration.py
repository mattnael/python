import numpy as np

# Fungsi Romberg Integration
def integrate_romberg(f, a, b):
    try:
        # Cek apakah batas valid
        if a == b:
            return 'NaN'

        max_k = 5  # Jumlah iterasi maksimal (bisa diubah)
        R = np.zeros((max_k, max_k))  # Tabel Romberg

        # Step 1: Hitung R[0, 0] pakai Trapezoid dengan 1 partisi
        h = b - a
        R[0, 0] = (h / 2) * (f(a) + f(b))

        # Step 2: Iterasi Romberg
        for k in range(1, max_k):
            h /= 2
            n = 2**k
            # Hitung jumlah nilai fungsi di titik tengah
            sum_mid = sum(f(a + (2*i - 1)*h) for i in range(1, 2**(k-1)+1))
            R[k, 0] = 0.5 * R[k-1, 0] + h * sum_mid

            # Richardson extrapolation
            for j in range(1, k+1):
                R[k, j] = R[k, j-1] + (R[k, j-1] - R[k-1, j-1]) / (4**j - 1)

            # Cek apakah hasil NaN/tak hingga
            if not np.isfinite(R[k, k]):
                return 'NaN'

        return R[max_k - 1, max_k - 1]

    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return 'NaN'

try:
    # Input fungsi dari user dalam bentuk string
    fungsi_str = input("Masukkan fungsi f(x) (contoh: x**2 + 3*x): ")

    # Input batas integrasi
    a = float(input("Masukkan batas bawah a: "))
    b = float(input("Masukkan batas atas b: "))

    # Input jumlah partisi
    n = int(input("Masukkan jumlah partisi n: "))

    # Bikin fungsi dari input string
    f = lambda x: eval(fungsi_str, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "exp": np.exp, "log": np.log})

    # Hitung dan tampilkan hasil
    hasil = integrate_trapezoid(f, a, b, n)
    print(f"Hasil integrasi: {hasil}")

except Exception as e:
    print("Terjadi kesalahan input atau perhitungan. Hasil: NaN")