import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("queue_data.csv")

# Tarih/saat sütunlarını dönüştür
df['arrival_time'] = pd.to_datetime(df['arrival_time'], errors='coerce')
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
df['finish_time'] = pd.to_datetime(df['finish_time'], errors='coerce')

df['service_time'] = (df['finish_time'] - df['start_time']).dt.total_seconds() / 60




# Negatif bekleme süresi kontrolü
negative_wait_rows = df[df['wait_time'] < 0]

# Mantıksal kontroller
start_before_arrival = df[df['start_time'] < df['arrival_time']]
finish_before_start = df[df['finish_time'] < df['start_time']]

# Sonuçları yazdır
print("🔎 Hata Denetimi Sonuçları:")
print(f"- Negatif bekleme süresi olan kayıt sayısı: {len(negative_wait_rows)}")
print(f"- Geliş saatinden önce başlamış hizmetler: {len(start_before_arrival)}")
print(f"- Hizmetten önce bitmiş çağrılar: {len(finish_before_start)}")

df_clean = df[df['wait_time'] >= 0].copy()

print(f"\n✅ Temizlenmiş veri kümesinde kalan satır sayısı: {len(df_clean)}")
df_clean.to_csv("queue_data_clean.csv", index=False)


