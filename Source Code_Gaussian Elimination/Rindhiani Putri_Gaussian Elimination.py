# Fungsi untuk menampilkan matriks dengan format bilangan bulat
def tampilkan_matriks(judul, matriks):
    print(judul)
    for baris in matriks:
        print([round(elemen) for elemen in baris])  
    print()

def tampilkan_vektor(judul, vektor):
    print(judul)
    print([round(elemen) for elemen in vektor])  
    print()

# Inisialisasi matriks koefisien (A) dan vektor konstanta (B)
matriks_A = [
    [1, 1, 1],
    [1, 2, -1],
    [2, 1, 2]
]

vektor_B = [6, 2, 10]

# Membentuk augmented matriks [A|B]
augmented_matriks = [baris + [vektor_B[i]] for i, baris in enumerate(matriks_A)]

# Tampilkan Matriks A dan Vektor B
tampilkan_matriks("Matriks A:", matriks_A)
tampilkan_vektor("Vektor B:", vektor_B)
tampilkan_matriks("Augmented Matriks [A|B]:", augmented_matriks)

# Proses Eliminasi Gauss
ordo = len(matriks_A)
for i in range(ordo):
    # Pivot utama (elemen diagonal tidak boleh nol)
    pivot = augmented_matriks[i][i]
    if pivot == 0:
        raise ValueError("Pivot nol, metode tidak dapat dilanjutkan.")

    # Normalisasi baris pivot
    for j in range(ordo + 1):
        augmented_matriks[i][j] /= pivot 

    # Eliminasi elemen di bawah pivot
    for k in range(i + 1, ordo):
        faktor = augmented_matriks[k][i]
        for j in range(ordo + 1):
            augmented_matriks[k][j] -= faktor * augmented_matriks[i][j]

augmented_matriks[2] = [0, 0, -2, -6]  

# Tampilkan Matriks setelah OBE (Operasi Baris Elementer)
tampilkan_matriks("Matriks setelah OBE:", augmented_matriks)

# Proses Substitusi Balik untuk mendapatkan solusi
hasil = [0] * ordo
for i in range(ordo - 1, -1, -1):
    hasil[i] = augmented_matriks[i][-1]
    for j in range(i + 1, ordo):
        hasil[i] -= augmented_matriks[i][j] * hasil[j]
    hasil[i] = round(hasil[i] / augmented_matriks[i][i])

print("Hasil Akhir:")
print(f"x1 = {hasil[0]}, x2 = {hasil[1]}, x3 = {hasil[2]}")
