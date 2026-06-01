import pandas as pd
import random
import pandas as pd
import random
import os

random.seed(42)
rows = []

for _ in range(300):
    ekran = random.randint(0, 8)
    kafein = random.randint(0, 400)
    stres = random.randint(1, 10)
    uyku = round(random.uniform(3, 10), 1)

    if ekran >= 5 or kafein >= 200 or stres >= 7 or uyku <= 5:
        etiket = "kotu"
    elif ekran <= 2 and kafein <= 80 and stres <= 4 and uyku >= 7:
        etiket = "iyi"
    else:
        etiket = "orta"

    rows.append([ekran, kafein, stres, uyku, etiket])

os.makedirs(r"C:\Users\Tufan\Desktop\uyku_projesi\data", exist_ok=True)

df = pd.DataFrame(
    rows, columns=["ekran_suresi", "kafein", "stres", "uyku_suresi", "etiket"]
)
df.to_csv(r"C:\Users\Tufan\Desktop\uyku_projesi\data\uyku_verisi.csv", index=False)
print("Veri seti olusturuldu:", len(df), "satir")
