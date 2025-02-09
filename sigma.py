import sys

n = int(input("Masukkan jumlah angka yang ingin dihitung sigmanya : "));
total = 0;
for i in range(1, n + 1): 
  x = int(input(f"Masukkan angka ke {i}: "));
  total += x;

print(f"Sigma dari semua angka tersebut adalah : {total}");

input("Tekan Enter untuk keluar...")