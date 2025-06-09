import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

# baca excel
df = pd.read_csv("MATH6192031_AoL Data.csv")

# variabel waktu: 0, 1, 2, ...
t = np.arange(len(df))
y = df['Number of bags'].values

# Regresi polinomial degree 6
degree = 6
koefisien = np.polyfit(t, y, degree)
model_polinomial = np.poly1d(koefisien)

# Tampilkan model matematis
print("📈 Model Regresi Polinomial:")
print(model_polinomial)

# Evaluasi akurasi model
y_prediksi = model_polinomial(t)
rmse = np.sqrt(mean_squared_error(y, y_prediksi))
r2 = r2_score(y, y_prediksi)

print(f"\nEvaluasi Akurasi:")
print(f"rmse: {rmse:.2f}")
print(f"R^2: {r2:.4f}")

# Prediksi
t_future= np.arange(t[-1] + 1, t[-1] + 100)
y_future = model_polinomial(t_future)

# Cek 25000
batas = 25000
lewat_batas= np.where(y_future > batas)[0]

if len(lewat_batas) > 0:
    bulan_lewat_batas = t_future[lewat_batas[0]]
    mulai_bangun = bulan_lewat_batas - 13 # 13 dari  "need at least 13 months"
    print(f"\nProduksi > 25.000 tas pada bulan ke-{bulan_lewat_batas}")
    print(f"Mulai bangun gudang pada bulan ke-{mulai_bangun}")
else:
    print("\n Produksi tidak melebihi 25.000 tas dalam 100 bulan ke depan.")

# Grafik
plt.scatter(t, y, label='Data Aktual')
plt.plot(t, model_polinomial(t), color='red', label='Regresi Polinomial')
plt.xlabel("Bulan ke-")
plt.ylabel("Jumlah Tas")
plt.legend()
plt.grid(True)
plt.show()
