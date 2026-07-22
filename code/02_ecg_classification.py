import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Практическое задание: классификация учебных ЭКГ-признаков.
# Студент обучает простую модель и объясняет метрики качества.

data = pd.read_csv("data/ecg/ecg_features_50.csv")
X = data.drop(columns=["sample_id", "label"])
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("Матрица ошибок:")
print(confusion_matrix(y_test, y_pred))
print("Отчёт классификации:")
print(classification_report(y_test, y_pred, target_names=["норма", "патология/аритмия"]))
print("ROC-AUC:", round(roc_auc_score(y_test, y_prob), 3))
