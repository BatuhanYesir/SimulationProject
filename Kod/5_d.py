import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Temiz veriyi yükle
df_clean = pd.read_csv("queue_data_clean.csv")

df_clean['arrival_time'] = pd.to_datetime(df_clean['arrival_time'], errors='coerce')
df_clean['start_time'] = pd.to_datetime(df_clean['start_time'], errors='coerce')
df_clean['finish_time'] = pd.to_datetime(df_clean['finish_time'], errors='coerce')




# Sayısal tiplere zorla (gerekliyse)
df_clean['wait_time'] = pd.to_numeric(df_clean['wait_time'], errors='coerce')
df_clean['service_time'] = pd.to_numeric(df_clean['service_time'], errors='coerce')

# Veri tiplerini kontrol et
print("📋 Veri Tipleri:\n")
print(df_clean.dtypes)

# Temel istatistikler
print("\n📈 Temel İstatistikler:\n")
print(df_clean[['wait_time', 'service_time']].describe())

# Histogram: Bekleme Süresi
plt.figure(figsize=(8, 5))
sns.histplot(df_clean['wait_time'].dropna(), bins=20, kde=True, color='skyblue')
plt.axvline(df_clean['wait_time'].mean(), color='red', linestyle='--', label='Ortalama')
plt.title("Bekleme Süresi Dağılımı")
plt.xlabel("Bekleme Süresi (dakika)")
plt.ylabel("Frekans")
plt.legend()
plt.show()

# Kutu Grafiği: Hizmet Süresi
plt.figure(figsize=(6, 4))
sns.boxplot(y=df_clean['service_time'].dropna(), color='lightgreen')
plt.title("Hizmet Süresi Kutu Grafiği")
plt.ylabel("Hizmet Süresi (dakika)")
plt.show()

# Korelasyon Matrisi
correlation = df_clean[['wait_time', 'service_time']].corr()
print("\n🔗 Korelasyon Matrisi:\n")
print(correlation)
