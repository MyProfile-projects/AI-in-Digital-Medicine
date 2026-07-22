import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Практическое задание: расчёт Dice и IoU для масок сегментации.

true_mask = pd.read_csv("data/segmentation/mask_true_1.csv", header=None).values
pred_mask = pd.read_csv("data/segmentation/mask_pred_1.csv", header=None).values

intersection = np.logical_and(true_mask == 1, pred_mask == 1).sum()
union = np.logical_or(true_mask == 1, pred_mask == 1).sum()

dice = 2 * intersection / ((true_mask == 1).sum() + (pred_mask == 1).sum())
iou = intersection / union

print("Dice coefficient:", round(dice, 3))
print("IoU:", round(iou, 3))

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(true_mask, cmap="gray"); axes[0].set_title("Эталонная маска")
axes[1].imshow(pred_mask, cmap="gray"); axes[1].set_title("Предсказанная маска")
for ax in axes: ax.axis("off")
plt.tight_layout(); plt.show()
