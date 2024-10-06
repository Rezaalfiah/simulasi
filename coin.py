import random
angka = 0
gambar = 0

for i in range(1000000):  # Satu juta kali putaran
    flip = random.randint(1, 2) #menghasilkan nilai random antara 1 dan 2
    if flip == 1:
        angka += 1
    else:
        gambar += 1

# Menghitung persentase
total_putaran = angka + gambar
angka_persentase = (angka / total_putaran) * 100
gambar_persentase = (gambar / total_putaran) * 100

#memunculkan angka, gambar, total putaran dan persentase muncul koin angka dan gambar
print(f"Angka: {angka}, Gambar: {gambar}, Total putaran: {total_putaran}")
print(f"Persentase muncul Angka: {angka_persentase:.2f}%")
print(f"Persentase muncul Gambar: {gambar_persentase:.2f}%")