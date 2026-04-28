# 🚲 Bike Sharing Dashboard

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan musim, kondisi cuaca, jenis hari, dan jam penggunaan.

Dashboard ini dibuat menggunakan **Streamlit** untuk memvisualisasikan data Bike Sharing pada periode **2011–2012** agar lebih mudah dipahami.

---

## 📊 Pertanyaan Bisnis

1. Musim dan kondisi cuaca apa dengan penyewaan tertinggi & terendah?
2. Jam berapa penyewaan tertinggi pada hari kerja vs non-kerja?

---

## 📁 Struktur Folder
submission/
├── dashboard/
│ ├── main_data.csv
│ └── dashboard.py
├── data/
│ ├── day.csv
│ └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt


---

## ⚙️ Setup Environment

### 1. Clone Repository

```bash
git clone <repository-url>
cd submission
```

### 2. Virtual Environment

```bash
python -m venv venv
```

```bash
#Windows
venv\Scripts\activate
```

```bash
#Mac / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Dashboard

```bash
streamlit run dashboard/dashboard.py
```

### 5. Fitur Dashboard

- Ringkasan metrik
- Analisis berdasarkan musim
- Analisis berdasarkan cuaca
- Pola per jam
- Hari kerja vs non-kerja
- Kategori demand
- Filter interaktif

### 6. Insight

- Musim Fall tertinggi
- Hari kerja: pagi & sore
- Cuaca cerah paling tinggi
- Hari libur: siang–sore

### 7. Rekomendasi

- Tambah sepeda saat demand tinggi
- Fokus saat cuaca cerah
- Optimalkan jam sibuk, 08.00, 17.00–18.00

### 8. Tools

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

### 9. Requirements

- pandas
- matplotlib
- seaborn
- streamlit