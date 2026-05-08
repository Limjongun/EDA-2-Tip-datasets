# EDA-2-Tip-datasets
exploratory data analyst , preparation and visualize data ,outliers handling 
FINAL INSIGHT TIPS DATASET:

1. Dataset tips memiliki 244 baris dan 7 kolom.
   Kolom numerik utama adalah total_bill, tip, dan size.
   Kolom kategorikal utama adalah sex, smoker, day, dan time.

2. Dataset tidak memiliki missing value.
   Artinya, dari sisi kelengkapan data, dataset ini cukup bersih.

3. Terdapat 1 baris duplikat.
   Namun karena dataset ini adalah data transaksi sederhana,
   duplikasi belum tentu berarti data salah.
   Perlu konteks tambahan sebelum menghapusnya.

4. Pelanggan male lebih banyak dibanding female.
   Pelanggan non-smoker lebih banyak dibanding smoker.

5. Transaksi paling banyak terjadi pada Saturday,
   dan waktu transaksi paling dominan adalah Dinner.

6. Distribusi total_bill dan tip cenderung right-skewed.
   Artinya, mayoritas transaksi bernilai kecil sampai sedang,
   tetapi ada beberapa transaksi dengan nilai besar.

7. total_bill dan tip memiliki hubungan positif.
   Semakin besar total_bill, tip cenderung ikut meningkat.

8. Dinner cenderung memiliki total_bill lebih tinggi dibanding Lunch.
   Ini bisa menunjukkan bahwa transaksi makan malam lebih besar,
   baik karena jumlah pesanan lebih banyak atau ukuran grup lebih besar.

9. Sunday terlihat memiliki median tip yang cukup tinggi.
   Namun insight ini perlu dibandingkan lagi dengan total_bill dan size
   agar tidak salah menyimpulkan.

10. Beberapa kolom numerik memiliki outlier.
    Outlier pada dataset tips tidak selalu buruk,
    karena bisa merepresentasikan transaksi besar yang valid.

11. Capping dapat digunakan untuk membatasi nilai ekstrem,
    tetapi keputusan handling outlier harus disesuaikan dengan tujuan analisis.

12. Dataset tips cocok untuk latihan EDA karena memiliki:
    - data numerik
    - data kategorikal
    - visualisasi distribusi
    - hubungan antar variabel
    - korelasi
    - outlier detection dan handling
