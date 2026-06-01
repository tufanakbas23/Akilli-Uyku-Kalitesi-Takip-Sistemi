import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

df = pd.read_csv(r"C:\Users\Tufan\Desktop\uyku_projesi\data\uyku_verisi.csv")

X = df[["ekran_suresi", "kafein", "stres", "uyku_suresi"]]
y = df["etiket"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
print("Confusion Matrix:\n", confusion_matrix(y_test, model.predict(X_test)))

joblib.dump(model, r"C:\Users\Tufan\Desktop\uyku_projesi\model.pkl")
print("model.pkl kaydedildi")
