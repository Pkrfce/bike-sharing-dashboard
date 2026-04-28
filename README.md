# Bike Sharing Dashboard

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan musim, cuaca, jenis hari, dan jam penggunaan. Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari data harian dan data per jam.

## Struktur Folder

```text
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

Cara Menjalankan Dashboard

Install library yang dibutuhkan:
pip install -r requirements.txt

Jalankan dashboard:
streamlit run dashboard/dashboard.py

Pertanyaan Bisnis
1.Pada periode 2011–2012, musim dan kondisi cuaca mana yang menghasilkan rata-rata jumlah penyewaan sepeda harian tertinggi dan terendah?

2.Pada periode 2011–2012, pada jam berapa permintaan penyewaan sepeda paling tinggi pada hari kerja dan hari non-kerja?

Insight Utama
1.Musim Fall memiliki rata-rata penyewaan harian tertinggi.
2.Cuaca cerah menghasilkan rata-rata penyewaan paling tinggi.
3.Pada hari kerja, permintaan tertinggi terjadi pada jam berangkat dan pulang kerja.
4.Pada hari non-kerja, permintaan lebih tinggi pada siang hingga sore hari.

Rekomendasi
Perusahaan sebaiknya menambah ketersediaan sepeda pada musim dan jam dengan permintaan tinggi, terutama saat cuaca cerah, hari kerja pukul 08.00 dan 17.00–18.00, serta hari non-kerja pada siang hingga sore hari.