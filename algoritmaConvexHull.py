import matplotlib.pyplot as plt

# Fungsi untuk menghitung cross product (orientasi tiga titik)
def hitung_cross_product(titik_o, titik_a, titik_b):
    return (titik_a[0] - titik_o[0]) * (titik_b[1] - titik_o[1]) - (titik_a[1] - titik_o[1]) * (titik_b[0] - titik_o[0])

# Fungsi untuk mencari convex hull dari sekumpulan titik
def cari_convex_hull(titik_titik):
    # Jika jumlah titik kurang dari atau sama dengan 3, kembalikan semua titik
    if len(titik_titik) <= 3:
        return titik_titik
    
    # Urutkan titik berdasarkan koordinat x (dan y jika x sama)
    titik_titik = sorted(titik_titik)
    
    # Fungsi rekursif untuk mencari convex hull
    def bagi_dan_taklukkan(titik_titik):
        if len(titik_titik) <= 3:
            return titik_titik
        
        # Bagi titik menjadi dua bagian
        tengah = len(titik_titik) // 2
        hull_kiri = bagi_dan_taklukkan(titik_titik[:tengah])
        hull_kanan = bagi_dan_taklukkan(titik_titik[tengah:])
        
        # Gabungkan dua convex hull
        return gabungkan(hull_kiri, hull_kanan)
    
    # Fungsi untuk menggabungkan dua convex hull
    def gabungkan(hull_kiri, hull_kanan):
        # Temukan titik paling kanan dari hull kiri
        # dan titik paling kiri dari hull kanan
        indeks_titik_kanan_hull_kiri = max(range(len(hull_kiri)), key=lambda i: hull_kiri[i][0])
        indeks_titik_kiri_hull_kanan = min(range(len(hull_kanan)), key=lambda i: hull_kanan[i][0])
        
        # Temukan upper tangent
        upper_kiri, upper_kanan = indeks_titik_kanan_hull_kiri, indeks_titik_kiri_hull_kanan
        while True:
            upper_kiri_baru = upper_kiri
            upper_kanan_baru = upper_kanan
            for i in range(len(hull_kiri)):
                if hitung_cross_product(hull_kanan[upper_kanan], hull_kiri[upper_kiri], hull_kiri[i]) > 0:
                    upper_kiri_baru = i
            for i in range(len(hull_kanan)):
                if hitung_cross_product(hull_kiri[upper_kiri], hull_kanan[upper_kanan], hull_kanan[i]) < 0:
                    upper_kanan_baru = i
            if upper_kiri_baru == upper_kiri and upper_kanan_baru == upper_kanan:
                break
            upper_kiri, upper_kanan = upper_kiri_baru, upper_kanan_baru
        
        # Temukan lower tangent
        lower_kiri, lower_kanan = indeks_titik_kanan_hull_kiri, indeks_titik_kiri_hull_kanan
        while True:
            lower_kiri_baru = lower_kiri
            lower_kanan_baru = lower_kanan
            for i in range(len(hull_kiri)):
                if hitung_cross_product(hull_kanan[lower_kanan], hull_kiri[lower_kiri], hull_kiri[i]) < 0:
                    lower_kiri_baru = i
            for i in range(len(hull_kanan)):
                if hitung_cross_product(hull_kiri[lower_kiri], hull_kanan[lower_kanan], hull_kanan[i]) > 0:
                    lower_kanan_baru = i
            if lower_kiri_baru == lower_kiri and lower_kanan_baru == lower_kanan:
                break
            lower_kiri, lower_kanan = lower_kiri_baru, lower_kanan_baru
        
        # Gabungkan titik-titik dari hull kiri, upper tangent, hull kanan, dan lower tangent
        hull_gabungan = []
        for i in range(upper_kiri + 1):
            hull_gabungan.append(hull_kiri[i])
        for i in range(upper_kanan, len(hull_kanan)):
            hull_gabungan.append(hull_kanan[i])
        for i in range(lower_kanan + 1):
            hull_gabungan.append(hull_kanan[i])
        for i in range(lower_kiri, len(hull_kiri)):
            hull_gabungan.append(hull_kiri[i])
        
        # Hapus duplikat dan kembalikan hasil
        return list(dict.fromkeys(hull_gabungan))
    
    return bagi_dan_taklukkan(titik_titik)

# Contoh penggunaan
titik_titik = [(0, 3), (1, 1), (2, 3.5), (2, 3), (4, 4), (3.5, 1.5), (0, 0), (2, 2), (1, 2), (3, 1), (3, 3)]
hull = cari_convex_hull(titik_titik)

# Plot titik dan convex hull
x = [titik[0] for titik in titik_titik]
y = [titik[1] for titik in titik_titik]
hull_x = [titik[0] for titik in hull]
hull_y = [titik[1] for titik in hull]

plt.scatter(x, y, label="Titik Acak")
plt.plot(hull_x + [hull_x[0]], hull_y + [hull_y[0]], 'r-', label="Convex Hull")
plt.legend()
plt.title(f"Convex Hull")
plt.show()