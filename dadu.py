import random

# Input jumlah lemparan dan jumlah sisi dadu
jmlh_lemparan = int(input("Jumlah lemparan: "))
if jmlh_lemparan <= 0:
    print("Harus melakukan setidaknya sekali lemparan")
    quit()

angka = int(input("Masukkan jumlah sisi pada dadu: "))
if angka <= 0:
    print("Angka harus lebih dari 0")
    quit()

# Simpan hasil lemparan
putaran = []
for i in range(jmlh_lemparan):
    face = random.randint(1, angka)
    putaran.append(face)

# Tampilkan hasil lemparan
print("Hasil lemparan:", putaran)

# Hitung berapa kali setiap angka muncul
frekuensi = {}
for i in range(1, angka + 1):
    frekuensi[i] = 0  # Set awal jumlah kemunculan tiap angka jadi 0

for hasil in putaran:
    frekuensi[hasil] += 1  # Tambah 1 setiap kali angka muncul

# Hitung persentase kemunculan tiap angka
persentase = {}
for i in range(1, angka + 1):
    persentase[i] = (frekuensi[i] / jmlh_lemparan) * 100

# Tampilkan persentase kemunculan tiap angka
print("\nPersentase kemunculan setiap angka:")
for i in range(1, angka + 1):
    print(f"Angka {i}: {persentase[i]:.2f}%")
