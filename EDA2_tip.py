# ============================================================
# EDA TIPS DATASET
# Exploratory Data Analysis pada Dataset Tips
# ============================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# 1. LOAD DATASET
# ============================================================

# Load dataset tips dari seaborn
# Dataset ini berisi data transaksi restoran:
# total_bill, tip, sex, smoker, day, time, dan size
df = sns.load_dataset('tips')

# Menampilkan 5 data pertama
print("Head:")
print(df.head())

# Menampilkan 5 data terakhir
print("Tail:")
print(df.tail())


# ============================================================
# 2. DATA OVERVIEW
# ============================================================

# Melihat jumlah baris dan kolom
print("Shape dataset:")
print(df.shape)

# Melihat nama-nama kolom
print("Kolom dataset:")
print(df.columns)

# Melihat informasi dataset:
# - tipe data
# - jumlah non-null
# - jumlah kolom
# - penggunaan memory
print("Info dataset:")
print(df.info())

# Melihat statistik deskriptif untuk kolom numerik
print("Statistik deskriptif:")
print(df.describe())

# Insight awal:
# Dataset tips memiliki 244 baris dan 7 kolom.
# Kolom numerik: total_bill, tip, size.
# Kolom kategorikal: sex, smoker, day, time.
# Dari info dataset, seluruh kolom memiliki jumlah non-null yang lengkap,
# sehingga tidak terlihat adanya missing value.


# ============================================================
# 3. CEK MISSING VALUE
# ============================================================

# Mengecek jumlah missing value per kolom
print("Missing value per kolom:")
print(df.isnull().sum())

# Menghitung persentase missing value per kolom
missing_percent = df.isnull().sum() / len(df) * 100

print("Persentase missing value:")
print(missing_percent)

# Insight:
# Tidak ada missing value pada dataset ini.
# Semua kolom memiliki persentase missing value 0%.
# Artinya, dataset sudah cukup bersih dari sisi kelengkapan data.


# ============================================================
# 4. CEK DATA DUPLIKAT
# ============================================================

# Mengecek jumlah data duplikat
print("Jumlah data duplikat:")
print(df.duplicated().sum())

# Menampilkan baris yang terdeteksi duplikat
duplicated_row = df[df.duplicated()]

print("Data duplikat:")
print(duplicated_row)

# Insight:
# Terdapat 1 baris yang terdeteksi sebagai duplikat.
# Namun pada dataset transaksi sederhana seperti tips,
# baris yang sama belum tentu benar-benar kesalahan,
# karena bisa saja dua transaksi memiliki nilai yang sama.
# Jadi data duplikat perlu dicek konteksnya sebelum dihapus.


# ============================================================
# 5. ANALISIS FITUR KATEGORIKAL
# ============================================================

# Fitur kategorikal adalah fitur yang berisi kategori.
# Pada dataset ini:
# sex    = jenis kelamin pelanggan
# smoker = status perokok atau bukan
# day    = hari transaksi
# time   = waktu makan, lunch atau dinner

categorical_column = ['sex', 'smoker', 'day', 'time']

for column in categorical_column:
    print(f"Value count untuk {column}:")
    print(df[column].value_counts())
    print()

    sns.countplot(data=df, x=column)
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel("Jumlah")
    plt.show()

# Insight:
# - Pelanggan male lebih banyak dibanding female.
# - Pelanggan non-smoker lebih banyak dibanding smoker.
# - Hari dengan transaksi paling banyak adalah Saturday.
# - Waktu makan paling dominan adalah Dinner.
# 
# Ini menunjukkan dataset lebih banyak merepresentasikan transaksi dinner,
# terutama pada akhir pekan.


# ============================================================
# 6. ANALISIS FITUR NUMERIK
# ============================================================

# Fitur numerik:
# total_bill = total tagihan
# tip        = jumlah tip
# size       = jumlah orang dalam satu meja/grup

numeric_column = ['total_bill', 'tip', 'size']

for column in numeric_column:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x=column, kde=True)

    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Insight:
# - total_bill paling banyak berada di range sekitar 10 sampai 20.
# - tip paling banyak berada di sekitar nilai kecil, sekitar 2 sampai 4.
# - size paling banyak berada pada ukuran 2 orang.
# - Distribusi total_bill dan tip cenderung right-skewed,
#   artinya mayoritas transaksi kecil sampai sedang,
#   tetapi ada beberapa transaksi dengan nilai sangat besar.


# ============================================================
# 7. HUBUNGAN TOTAL BILL DAN TIP
# ============================================================

# Scatterplot digunakan untuk melihat hubungan antara dua variabel numerik.
# Di sini kita ingin melihat apakah total tagihan berhubungan dengan tip.

sns.scatterplot(data=df, x='total_bill', y='tip')
plt.title("Hubungan Total Bill dan Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Insight:
# Titik-titik cenderung naik ke kanan.
# Artinya, semakin besar total_bill, tip juga cenderung meningkat.
# Namun titik paling banyak tetap berkumpul pada area total_bill rendah sampai sedang.


# ============================================================
# 8. TOTAL BILL VS TIP BERDASARKAN SMOKER
# ============================================================

# hue='smoker' digunakan untuk membedakan warna titik
# berdasarkan pelanggan smoker dan non-smoker.

sns.scatterplot(data=df, x='total_bill', y='tip', hue='smoker')
plt.title("Total Bill vs Tip Berdasarkan Smoker")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Insight:
# Secara umum, baik smoker maupun non-smoker tetap menunjukkan pola:
# semakin besar total_bill, tip cenderung ikut meningkat.
# Dari visual ini, status smoker tidak terlihat sebagai pembeda paling kuat
# dalam hubungan total_bill dan tip.


# ============================================================
# 9. BOXPLOT TIP BERDASARKAN HARI
# ============================================================

# Boxplot digunakan untuk melihat distribusi tip berdasarkan hari.
# Dari boxplot kita bisa melihat median, sebaran data, dan outlier.

sns.boxplot(data=df, x='day', y='tip')
plt.title("Distribusi Tip Berdasarkan Hari")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()

# Insight:
# Sunday terlihat memiliki median tip yang cukup tinggi.
# Hal ini bisa terjadi karena weekend biasanya memiliki transaksi makan
# yang lebih besar atau jumlah pelanggan/grup yang lebih banyak.
# Namun perlu dicek juga dengan total_bill dan size agar insight lebih kuat.


# ============================================================
# 10. BOXPLOT TOTAL BILL BERDASARKAN TIME
# ============================================================

# Membandingkan total_bill antara Lunch dan Dinner.

sns.boxplot(data=df, x='time', y='total_bill')
plt.title("Distribusi Total Bill Berdasarkan Time")
plt.xlabel("Time")
plt.ylabel("Total Bill")
plt.show()

# Insight:
# Dinner memiliki total_bill yang cenderung lebih besar dibanding Lunch.
# Ini masuk akal karena makan malam sering lebih ramai,
# bisa melibatkan grup lebih besar, dan total pesanan lebih tinggi.


# ============================================================
# 11. CORRELATION HEATMAP
# ============================================================

# Mengambil hanya kolom numerik
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Menghitung korelasi antar fitur numerik
correlation = numeric_df.corr()

print("Correlation matrix:")
print(correlation)

# Visualisasi korelasi menggunakan heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap Tips Dataset")
plt.show()

# Insight:
# - total_bill dan tip memiliki korelasi positif cukup kuat.
#   Artinya, semakin besar total_bill, tip cenderung semakin besar.
# - size juga berkorelasi positif dengan total_bill,
#   artinya semakin besar jumlah orang dalam grup,
#   total tagihan cenderung semakin tinggi.
# - Korelasi positif bukan berarti sebab-akibat mutlak,
#   tetapi menunjukkan hubungan linear antar variabel.


# ============================================================
# 12. DETEKSI OUTLIER MENGGUNAKAN IQR
# ============================================================

# IQR = Interquartile Range
# Rumus:
# IQR = Q3 - Q1
#
# Lower fence = Q1 - 1.5 * IQR
# Upper fence = Q3 + 1.5 * IQR
#
# Data dianggap outlier jika:
# data < lower_fence
# atau
# data > upper_fence

def detect_outlier_iqr(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    outliers = data[
        (data[column] < lower_fence) |
        (data[column] > upper_fence)
    ]

    print(f"\nOutlier detection untuk kolom: {column}")
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower fence:", lower_fence)
    print("Upper fence:", upper_fence)
    print("Jumlah outlier:", len(outliers))

    return lower_fence, upper_fence, outliers


# Menjalankan deteksi outlier untuk setiap kolom numerik
for column in numeric_column:
    lower, upper, outliers = detect_outlier_iqr(df, column)
    print(outliers)

# Insight:
# Outlier paling mungkin muncul pada total_bill, tip, dan size.
# Pada dataset restoran, outlier tidak selalu berarti data salah.
# Bisa saja transaksi tersebut benar-benar bernilai besar,
# misalnya grup pelanggan besar atau total tagihan tinggi.
# Karena itu, outlier perlu dianalisis konteksnya sebelum dihapus.


# ============================================================
# 13. VISUALISASI OUTLIER SEBELUM HANDLING
# ============================================================

# Boxplot digunakan untuk melihat outlier secara visual.

for column in numeric_column:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x=column)
    plt.title(f"Boxplot Sebelum Outlier Handling: {column}")
    plt.xlabel(column)
    plt.show()

# Insight:
# Boxplot membantu melihat titik-titik yang berada di luar whisker.
# Titik tersebut adalah kandidat outlier berdasarkan metode IQR.


# ============================================================
# 14. OUTLIER HANDLING DENGAN CAPPING
# ============================================================

# Capping adalah teknik membatasi nilai outlier.
# Nilai yang lebih kecil dari lower_fence akan diganti menjadi lower_fence.
# Nilai yang lebih besar dari upper_fence akan diganti menjadi upper_fence.
#
# Capping tidak menghapus data,
# tetapi membatasi nilai ekstrem agar tidak terlalu memengaruhi analisis/model.

df_capped = df.copy()

def cap_outlier_iqr(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    data[column] = np.where(
        data[column] < lower_fence,
        lower_fence,
        np.where(
            data[column] > upper_fence,
            upper_fence,
            data[column]
        )
    )

    return data


# Melakukan capping untuk setiap kolom numerik
for column in numeric_column:
    df_capped = cap_outlier_iqr(df_capped, column)


# ============================================================
# 15. MEMBANDINGKAN STATISTIK SEBELUM DAN SESUDAH CAPPING
# ============================================================

for column in numeric_column:
    print(f"\nStatistik sebelum capping {column}:")
    print(df[column].describe())

    print(f"\nStatistik setelah capping {column}:")
    print(df_capped[column].describe())

# Insight:
# Setelah capping, nilai maksimum pada kolom yang memiliki outlier
# akan menjadi lebih rendah atau lebih terkendali.
# Ini membantu mengurangi pengaruh nilai ekstrem terhadap analisis statistik.


# ============================================================
# 16. VISUALISASI SETELAH OUTLIER HANDLING
# ============================================================

for column in numeric_column:
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df_capped, x=column)
    plt.title(f"Boxplot Setelah Outlier Handling: {column}")
    plt.xlabel(column)
    plt.show()

# Insight:
# Setelah capping, outlier ekstrem akan berkurang atau hilang dari boxplot.
# Namun data asli tetap sebaiknya disimpan,
# karena pada analisis bisnis, outlier kadang justru berisi informasi penting.


# ============================================================
# 17. FINAL INSIGHT
# ============================================================

print("""
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
""")