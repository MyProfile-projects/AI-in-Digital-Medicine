import pandas as pd
import matplotlib.pyplot as plt

# Практическое задание: визуализировать учебный ЭЭГ-сигнал и описать его особенности.

file_path = "data/eeg/eeg_sample_1_alpha.csv"
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 4))
plt.plot(data["time_sec"], data["signal"], linewidth=1)
plt.xlabel("Время, с")
plt.ylabel("Амплитуда, усл. ед.")
plt.title("Учебный ЭЭГ-сигнал")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Контрольные вопросы:")
print("1. Выглядит ли сигнал регулярным?")
print("2. Есть ли участки, похожие на шум или артефакты?")
print("3. Почему для анализа ЭЭГ важно качество записи?")
print("4. Почему ИИ-модель для ЭЭГ должна проходить проверку на данных разных пациентов?")
