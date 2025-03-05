<h1> TUGAS INDIVIDU PERANCANGAN DAN ANALISIS ALGORITMA</h1>
<h3>Algoritma Convex-Hull Problems</h3>
<br>
<p>Algoritma convex-hull digunakan untuk menemukan convex hull dari sekumpulan titik dalam geometri komputasional. Convex-hull adalah himpunan cembung terkecil yang melingkupi semua titik, membentuk polygon cembung. </p>
<br><p>Algoritma convex-hull dengan pendekatan Divide and Conquer adalah salah satu metode yang efisien untuk menemukan himpunan cembung terkecil yang mencakup semua titik dalam suatu Kumpulan. Pendekatan ini membagi himpunan titik menjadi dua bagian yang lebih kecil, menyelesaikan masing-masing bagian secara rekursif, lalu menggabungkan hasilnya untuk membentuk Convex-Hull akhir.</p>
<br><p>Langkah-langkah algoritma convex-hull divide and conquer:<br>
1.	Divide (pembagian titik)<br>
•	Mengurutkan titik-titik berdasarkan koordoinat x untuk mempermudah pembagian. Pengurutan ini biasanya dilakukan menggunakna merge sort atau quicksort dengan kompleksitas O(n log n).<br>
•	Bagi Kumpulan titik mnejadi dua bagian yang kira-kira sama besar, bagian kiri (A) dan bagian kanan (B).<br>
•	Setiap bagian akan dihitung Convex-Hull nya secara terpisah menggunakan metode rekursif.<br>

2.	Conquer (Menyusun convex-hull dari masing-masing bagian)<br>
•	Gunakan algortima convex hull sederhana untuk menemukan hull dari masing-masing bagian. Biasanya menggunakan algoritma Graham’s Scan (O(nlogn)) digunakan untuk efisiensi yang lebih baik.<br>
•	Setelah mendapatkan convex hull dari bagian kiri dan kanan, Langkah berikutnya adalah menggabungkan keduanya.<br>

3.	Combine (menggabungkan dua convex hull menjadi satu)<br>
•	Cari garis singgung atas dan garis singgung bawah antara kedua Convex hull yang telah ditemukan.<br>
•	Gunaan binary search (O(log n)) untuk menemukan titik ekstrem yang membentuk garis singgung ini secara efisien.<br>
•	Titik-titik yang berada di dalam batas garis singgung dihapus karena tidak diperlukan dalam hasil akhir.<br>
•	Hasilnya adalah Convex Hull gabungan yang mencakup semua titik.<br>
</p>
