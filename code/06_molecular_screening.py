import pandas as pd

# Практическое задание: простое учебное ранжирование молекул-кандидатов.
# Это не фармакологическая модель, а демонстрация логики вычислительного отбора.

file_path = "data/molecules/molecules_demo.csv"
data = pd.read_csv(file_path)

print("Исходная таблица:")
print(data)

filtered = data[
    (data["activity_score"] >= 0.65) &
    (data["toxicity_risk"] <= 0.40) &
    (data["solubility_score"] >= 0.50)
].copy()

filtered["final_score"] = (
    0.5 * filtered["activity_score"] +
    0.3 * filtered["solubility_score"] -
    0.2 * filtered["toxicity_risk"]
)

filtered = filtered.sort_values("final_score", ascending=False)

print("Кандидаты после фильтрации и ранжирования:")
print(filtered[[
    "molecule_id", "smiles", "activity_score", "toxicity_risk",
    "solubility_score", "final_score"
]])

print("Контрольные вопросы:")
print("1. Какие молекулы прошли фильтр?")
print("2. Почему высокая активность недостаточна, если риск токсичности высокий?")
print("3. Что означает ADMET при разработке лекарств?")
print("4. Почему такой расчёт является только учебной моделью, а не доказательством эффективности препарата?")
