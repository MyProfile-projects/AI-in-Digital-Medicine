import pandas as pd
import matplotlib.pyplot as plt

# Практическое задание: визуализация учебного ЭКГ-сигнала.
# Студент строит график, описывает регулярность ритма, амплитуду и наличие шума.

file_path = "data/ecg/ecg_sample_1_norm.csv"
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 4))
plt.plot(data["time_sec"], data["signal"], linewidth=1)
plt.xlabel("Время, с")
plt.ylabel("Амплитуда, усл. ед.")
plt.title("Учебный ЭКГ-сигнал")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Контрольные вопросы:")
print("1. Видны ли регулярные пики?")
print("2. Есть ли выраженный шум?")
print("3. Какие ограничения имеет визуальная оценка сигнала?")
