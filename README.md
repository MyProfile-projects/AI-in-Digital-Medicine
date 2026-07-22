<div align="center">

<img src="assets/banner.svg" alt="AI in Digital Medicine" width="100%">

# AI in Digital Medicine

### Educational repository for artificial intelligence and machine learning in modern digital medicine

[![Python](https://img.shields.io/badge/Python-3.10%2B-111827?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-ready-7C3AED?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Educational](https://img.shields.io/badge/Purpose-Educational-34D399?style=for-the-badge)](#important-notice)
[![Digital Medicine](https://img.shields.io/badge/Field-Digital%20Medicine-0F172A?style=for-the-badge)](#learning-modules)

</div>

---

## Overview

**AI in Digital Medicine** is an educational repository accompanying a textbook on artificial intelligence and machine learning in contemporary medicine. It contains compact Python templates and demonstration datasets for practical work with biomedical signals, medical-image segmentation metrics, clinical text retrieval, neurophysiological data, and molecular screening.

The repository is designed for medical students, residents, clinicians, and educators who want to understand not only how code runs, but also what the result means clinically.

---

## Important notice

> This repository is intended **only for educational use**.  
> The code and datasets are demonstration materials and must not be used for diagnosis, treatment, prognosis, triage, medical decision-making, or validation of clinical AI systems.

All datasets included here are synthetic or demonstrational. If real clinical data are used in teaching, they must be properly anonymized and handled according to institutional, ethical, and legal requirements.

---

## Learning modules

| Module | Topic | Code template | Main skill |
|---|---|---|---|
| 01 | ECG signal visualization | `code/01_ecg_visualization.py` | Reading and plotting biomedical signals |
| 02 | ECG classification | `code/02_ecg_classification.py` | Interpreting confusion matrix, sensitivity, specificity, F1-score, ROC-AUC |
| 03 | Medical-image segmentation | `code/03_dice_segmentation.py` | Calculating Dice coefficient and IoU |
| 04 | Clinical NLP / RAG | `code/04_mini_rag.py` | Retrieval-based grounding of language-model answers |
| 05 | EEG / BCI signals | `code/05_eeg_visualization.py` | Visual analysis of neurophysiological data and artifacts |
| 06 | Molecular screening | `code/06_molecular_screening.py` | Simple candidate ranking using ADMET-like criteria |

---

## Repository structure

```text
AI-in-Digital-Medicine/
├── assets/
│   └── banner.svg
├── code/
├── data/
│   ├── ecg/
│   ├── eeg/
│   ├── segmentation/
│   ├── nlp/
│   └── molecules/
├── docs/
├── notebooks/
├── requirements.txt
└── README.md
```

---

## Quick start

```bash
git clone https://github.com/MyProfile-projects/AI-in-Digital-Medicine.git
cd AI-in-Digital-Medicine
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate     # Windows
pip install -r requirements.txt
python code/01_ecg_visualization.py
```

---

## What should I do here?

If you opened this repository from the textbook or course materials, you can use it to run small practical examples in digital medicine. You do not need to build an AI system from scratch. Choose a topic, open the corresponding script, run it, and interpret the result.

## How to use this repository

This repository contains educational Python code templates and synthetic datasets for practical assignments in AI and digital medicine.

If you are visiting this repository for the first time, follow these steps:

1. **Choose a learning module**

   Open the table above and select the topic you want to study:

   - ECG signal visualization;
   - ECG classification;
   - medical-image segmentation;
   - clinical NLP / RAG;
   - EEG / BCI signal visualization;
   - molecular screening.

2. **Open the corresponding code file**

   Go to the `code/` folder and open the Python file for the selected topic.

   For example:

   - `code/01_ecg_visualization.py` — ECG signal visualization;
   - `code/02_ecg_classification.py` — ECG classification;
   - `code/03_dice_segmentation.py` — Dice and IoU calculation;
   - `code/04_mini_rag.py` — simple retrieval-based search;
   - `code/05_eeg_visualization.py` — EEG signal visualization;
   - `code/06_molecular_screening.py` — molecular candidate ranking.

3. **Check the required dataset**

   Each code template uses a file from the `data/` folder.

   For example:

   - ECG files are located in `data/ecg/`;
   - segmentation masks are located in `data/segmentation/`;
   - synthetic clinical text fragments are located in `data/nlp/`;
   - EEG files are located in `data/eeg/`;
   - molecular data are located in `data/molecules/`.

4. **Install the required Python libraries**

   The basic version requires:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the selected script from the repository root**

   For example:

   ```bash
   python code/01_ecg_visualization.py
   ```

   It is important to run the script from the main repository folder so that the relative paths to `data/` work correctly.

6. **Look at the result**

   Depending on the module, the script will produce:

   - a graph of a biomedical signal;
   - classification metrics;
   - Dice / IoU values;
   - retrieved text fragments;
   - a ranked table of molecular candidates.

7. **Answer the questions in the code**

   At the end of each script there are short control questions. They help interpret the result and understand the limitations of the method.

8. **Remember the educational purpose**

   The code and datasets are simplified educational examples. They are not intended for diagnosis, treatment, prognosis, triage, or clinical decision-making.

---

## For students

When completing an assignment, describe:

- what data were used;
- what the code calculated or visualized;
- what the output means;
- what limitations the method has;
- why the result cannot be treated as a clinical conclusion.

---

## For instructors

Before class, it is recommended to:

- check that all scripts run from the repository root;
- verify that file paths to `data/` are correct;
- prepare Jupyter or Google Colab versions if needed;
- explain that synthetic data are used for training purposes;
- evaluate both technical execution and clinical interpretation.

Suggested assessment structure:

| Criterion | Weight |
|---|---:|
| Code execution | 20% |
| Understanding of data structure | 20% |
| Interpretation of metrics or plots | 25% |
| Clinical meaning of the conclusion | 25% |
| Clarity and accuracy of the report | 10% |

---

<div align="center">

**Digital medicine requires not only intelligent algorithms, but also clinically responsible interpretation.**

</div>
