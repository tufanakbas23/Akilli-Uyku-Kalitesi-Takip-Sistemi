from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import sys

sys.path.insert(0, r"C:\Users\Tufan\Desktop\uyku_projesi")
from db import veritabanini_kur, tahmin_kaydet, gecmis_tahminleri_getir

app = Flask(__name__)
CORS(app)
model = joblib.load(r"C:\Users\Tufan\Desktop\uyku_projesi\model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    ekran = float(data["ekran_suresi"])
    kafein = float(data["kafein"])
    stres = float(data["stres"])
    uyku = float(data["uyku_suresi"])

    sonuc = model.predict([[ekran, kafein, stres, uyku]])[0]
    tahmin_kaydet(ekran, kafein, stres, uyku, sonuc)

    return jsonify({"durum": sonuc})


@app.route("/history")
def history():
    rows = gecmis_tahminleri_getir()
    return jsonify([dict(r) for r in rows])


if __name__ == "__main__":
    veritabanini_kur()
    app.run(debug=True)
