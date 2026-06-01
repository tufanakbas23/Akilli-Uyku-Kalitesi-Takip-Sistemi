# 🌙 Akıllı Uyku Kalitesi Tahmin Sistemi

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=flat-square&logo=react" />
  <img src="https://img.shields.io/badge/scikit--learn-RandomForest-orange?style=flat-square&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/SQLite-DB-003B57?style=flat-square&logo=sqlite" />
  <img src="https://img.shields.io/badge/Accuracy-98.33%25-brightgreen?style=flat-square" />
</p>

> Kullanıcının günlük alışkanlıklarına göre uyku kalitesini tahmin eden web tabanlı makine öğrenmesi uygulaması.

---

## ✨ Özellikler

- Makine öğrenmesi tabanlı uyku kalitesi tahmini
- Anlık tahmin üretimi
- SQLite veritabanına otomatik kayıt
- React tabanlı modern kullanıcı arayüzü
- Flask tabanlı REST API yapısı

---

## 🛠️ Teknoloji Yığını

| Katman | Teknoloji |
|---|---|
| Backend | Python, Flask, flask-cors |
| Makine Öğrenmesi | scikit-learn, joblib |
| Veritabanı | SQLite |
| Frontend | React, Vite, Bootstrap, Axios |

---

## 📁 Proje Yapısı

```bash
uyku_projesi/
├── app.py
├── train.py
├── generate_data.py
├── db.py
├── model.pkl
├── uyku_veritabani.db
├── data/
│   └── uyku_verisi.csv
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   └── main.jsx
    ├── package.json
    └── vite.config.js
```

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.10+
- Node.js 18+

### 1. Python bağımlılıklarını yükle

```bash
pip install flask flask-cors scikit-learn pandas joblib
```

### 2. Veri setini oluştur

```bash
python generate_data.py
```

### 3. Modeli eğit

```bash
python train.py
```

### 4. Backend'i başlat

```bash
python app.py
```

### 5. Frontend'i başlat (yeni terminal)

```bash
cd frontend
npm install
npm run dev
```

Tarayıcıda `http://localhost:5173` adresini aç.

---

## 📡 API

### `POST /predict`

**Request:**
```json
{
  "ekran_suresi": 6,
  "kafein": 250,
  "stres": 8,
  "uyku_suresi": 4
}
```

**Response:**
```json
{
  "durum": "kotu"
}
```

Olası değerler: `iyi` | `orta` | `kotu`

### `GET /history`

Tüm geçmiş tahminleri listeler.

---

## 📊 Model Performansı

- **Algoritma:** RandomForestClassifier
- **Veri Seti:** 300 satır sentetik veri, 4 özellik
- **Eğitim/Test:** %80 / %20
- **Accuracy:** %98.33

| | kotu | iyi | orta |
|---|---:|---:|---:|
| **kotu** | 1 | 0 | 0 |
| **iyi** | 0 | 46 | 0 |
| **orta** | 0 | 1 | 12 |

---

## 🗄️ Veritabanı Şeması

```sql
CREATE TABLE predictions (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    ekran_suresi REAL,
    kafein       REAL,
    stres        INTEGER,
    uyku_suresi  REAL,
    tahmin_sonuc TEXT,
    kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📄 Lisans

Bu proje akademik amaçlı geliştirilmiştir.
