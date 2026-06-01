import sqlite3

veritabanı_adi = r"C:\Users\Tufan\Desktop\uyku_projesi\uyku_veritabani.db"


def veritabanini_kur():
    baglanti = sqlite3.connect(veritabanı_adi)
    cursor = baglanti.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ekran_suresi REAL,
        kafein REAL,
        stres INTEGER,
        uyku_suresi REAL,
        tahmin_sonuc TEXT,
        kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    baglanti.commit()
    baglanti.close()
    print("Veritabani ve predictions tablosu olusturuldu!")


def tahmin_kaydet(ekran_suresi, kafein, stres, uyku_suresi, tahmin_sonuc):
    baglanti = sqlite3.connect(veritabanı_adi)
    cursor = baglanti.cursor()

    sorgu = """
    INSERT INTO predictions 
    (ekran_suresi, kafein, stres, uyku_suresi, tahmin_sonuc) 
    VALUES (?, ?, ?, ?, ?)
    """
    veriler = (ekran_suresi, kafein, stres, uyku_suresi, tahmin_sonuc)

    cursor.execute(sorgu, veriler)
    baglanti.commit()
    baglanti.close()
    print("Tahmin veritabanina kaydedildi.")


def gecmis_tahminleri_getir():
    baglanti = sqlite3.connect(veritabanı_adi)
    baglanti.row_factory = sqlite3.Row
    cursor = baglanti.cursor()

    cursor.execute("""
        SELECT id, ekran_suresi, kafein, stres, uyku_suresi, tahmin_sonuc, kayit_tarihi 
        FROM predictions 
        ORDER BY id DESC
    """)

    gecmis = cursor.fetchall()
    baglanti.close()
    return gecmis
