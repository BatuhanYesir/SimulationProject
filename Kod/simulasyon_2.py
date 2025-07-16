import numpy as np
import pandas as pd

def run_simulation(num_customers, arrival_rate, service_rate, seed=None):
    if seed is not None:
        np.random.seed(seed)

    interarrival_times = np.random.exponential(scale=1/arrival_rate, size=num_customers)
    arrival_times = np.cumsum(interarrival_times)
    service_times = np.random.exponential(scale=1/service_rate, size=num_customers)

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

    return {
        "avg_wait": np.mean(wait_times),
        "avg_queue": np.mean([w > 0 for w in wait_times]),
        "wait_times": wait_times
    }

# Deney parametreleri
scenarios = {
    "S1": {"λ": 0.1, "μ": 0.2},
    "S2": {"λ": 0.15, "μ": 0.15},
    "S3": {"λ": 0.2, "μ": 0.1}
}
num_customers = 100
num_trials = 30

results = []

for name, params in scenarios.items():
    waits = []
    queues = []
    for trial in range(num_trials):
        outcome = run_simulation(num_customers, params["λ"], params["μ"], seed=trial)
        waits.append(outcome["avg_wait"])
        queues.append(outcome["avg_queue"])
    
    results.append({
        "Senaryo": name,
        "λ": params["λ"],
        "μ": params["μ"],
        "ρ": round(params["λ"] / params["μ"], 2),
        "Ortalama Bekleme": round(np.mean(waits), 2),
        "Ortalama Kuyrukta Kalma Oranı": round(np.mean(queues), 2)
    })

# Sonuçları DataFrame olarak göster
df_results = pd.DataFrame(results)
print(df_results)
