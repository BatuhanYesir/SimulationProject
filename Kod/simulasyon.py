import numpy as np
import pandas as pd

# Parametreler
num_customers = 10               # Kaç müşteri benzetilecek
arrival_rate = 1 / 3             # Ortalama 3 dakikada 1 müşteri (lambda)
service_rate = 1 / 5             # Ortalama hizmet süresi 5 dakika (mu)

# Rastgele zamanlar üret
np.random.seed(42)
interarrival_times = np.random.exponential(scale=1/arrival_rate, size=num_customers)
arrival_times = np.cumsum(interarrival_times)
service_times = np.random.exponential(scale=1/service_rate, size=num_customers)

# Simülasyon
start_times = []
finish_times = []
wait_times = []

for i in range(num_customers):
    if i == 0:
        start_time = arrival_times[i]
    else:
        start_time = max(arrival_times[i], finish_times[i - 1])
    finish_time = start_time + service_times[i]
    wait_time = start_time - arrival_times[i]
    
    start_times.append(start_time)
    finish_times.append(finish_time)
    wait_times.append(wait_time)

# Sonuçları DataFrame olarak düzenle
sim_result = pd.DataFrame({
    "arrival_time": arrival_times,
    "start_time": start_times,
    "finish_time": finish_times,
    "interarrival_time": interarrival_times,
    "service_time": service_times,
    "wait_time": wait_times
})

print(sim_result.round(2))
