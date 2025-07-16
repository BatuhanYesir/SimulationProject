import pandas as pd
from scipy import stats

# Veriyi oku
df = pd.read_csv("queue_data.csv")

# Gerekli zaman sütunlarını dönüştür
df['arrival_time'] = pd.to_datetime(df['arrival_time'], errors='coerce')
df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
df['finish_time'] = pd.to_datetime(df['finish_time'], errors='coerce')

# Negatif veya NaN bekleme süresi olanları çıkar
df = df[(df['wait_time'] >= 0) & df['wait_time'].notna()]

# Hizmet süresi hesapla (dakika cinsinden)
df['service_time'] = (df['finish_time'] - df['start_time']).dt.total_seconds() / 60
df = df[df['service_time'].notna() & (df['service_time'] >= 0)]

# Burada dağılım testi yapılacak hedef değişkeni seç
target = df['wait_time']  # ya da df['service_time']

# Örneklem büyüklüğü kontrolü
if len(target) > 500:
    sample = target.sample(n=500, random_state=1)
else:
    sample = target

# Shapiro-Wilk testi (normallik testi)
shapiro_test = stats.shapiro(sample)
print("Shapiro-Wilk Testi:")
print(f"Test istatistiği: {shapiro_test.statistic:.4f}")
print(f"p-değeri: {shapiro_test.pvalue:.4f}")
