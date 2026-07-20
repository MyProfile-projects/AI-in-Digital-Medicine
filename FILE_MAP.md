# Карта файлов

| Задание | Код | Данные | Результат |
|---|---|---|---|
| Визуализация ЭКГ | `code/01_ecg_visualization.py` | `data/ecg/ecg_sample_*.csv` | График сигнала и краткая интерпретация |
| Классификация ЭКГ | `code/02_ecg_classification.py` | `data/ecg/ecg_features_50.csv` | Таблица метрик, ROC-AUC, вывод об accuracy |
| Сегментация | `code/03_dice_segmentation.py` | `data/segmentation/mask_true_*.csv`, `mask_pred_*.csv` | Dice, IoU, визуализация масок |
| Мини-RAG | `code/04_mini_rag.py` | `data/nlp/emk_fragments_synthetic.csv` | Топ найденных фрагментов |
| ЭЭГ | отдельное расширенное задание | `data/eeg/eeg_sample_*.csv` | График и оценка частотного диапазона |
