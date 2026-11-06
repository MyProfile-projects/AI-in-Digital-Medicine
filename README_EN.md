<div align="center">

<img src="assets/banner_eng.svg" alt="AI in Digital Medicine" width="100%">

### Educational code and synthetic datasets for learning artificial intelligence in modern medicine

**English** | [Русский](README.md)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter%20%2F%20Colab-ready-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Educational](https://img.shields.io/badge/Purpose-Educational-2E8B57?style=for-the-badge)](#important-notice)
[![Medical AI](https://img.shields.io/badge/Field-Digital%20Medicine-7B68EE?style=for-the-badge)](#learning-modules)

</div>

---

## 📋 Table of contents

- [Overview](#overview)
- [Important notice](#important-notice)
- [Learning modules](#learning-modules)
- [Repository structure](#repository-structure)
- [Quick start](#quick-start)
- [Recommended teaching workflow](#recommended-teaching-workflow)
- [Minimal software requirements](#minimal-software-requirements)
- [For students](#for-students)
- [For instructors](#for-instructors)
- [License and citation](#license-and-citation)

---

## Overview

**AI in Digital Medicine** is an educational repository accompanying a textbook on artificial intelligence and machine learning in contemporary medicine.  
It contains compact Python templates and demonstration datasets for practical work with biomedical signals, medical-image segmentation metrics, clinical text retrieval, neurophysiological data, and molecular screening.

The repository is designed primarily for **medical students, residents, clinicians, and educators** who are beginning to work with AI methods and want to understand not only how code runs, but also **what the result means clinically**.

---

## Important notice

> [!CAUTION]
> This repository is intended **only for educational use**.  
> The code and datasets are demonstration materials and must not be used for diagnosis, treatment, prognosis, triage, medical decision-making, or validation of clinical AI systems.

All datasets included here are synthetic or demonstrational. If real clinical data are used in teaching, they must be properly anonymized and handled according to institutional, ethical, and legal requirements.

---

## Learning modules

| Module | Topic | Code template | Main skill |
|:---:|---|---|---|
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
├── assets/                 # visual materials for README
├── code/                   # Python templates for practical assignments
├── data/                   # synthetic and demonstration datasets
│   ├── ecg/                # ECG signals and ECG feature table
│   ├── eeg/                # EEG signal examples
│   ├── segmentation/       # true/predicted binary masks
│   ├── nlp/                # synthetic clinical-text fragments
│   └── molecules/          # demonstration molecular table
├── docs/                   # teaching notes and assignment descriptions
├── notebooks/              # optional Jupyter / Colab versions
├── requirements.txt        # minimal Python dependencies
└── README.md
```

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/MyProfile-projects/AI-in-Digital-Medicine.git
cd AI-in-Digital-Medicine
```

### 2. Create an environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run a template

```bash
python code/01_ecg_visualization.py
```

---

## Recommended teaching workflow

1. Start with the clinical problem: **what question are we trying to answer?**
2. Open the corresponding dataset and discuss its structure.
3. Run the code template.
4. Interpret the output together with students.
5. Discuss limitations, possible sources of error, and clinical safety.
6. Ask students to write a short conclusion in medical language.

The goal is not programming from scratch, but understanding the connection between **data → algorithm → metric → clinical interpretation → limitation**.

---

## Minimal software requirements

- Python 3.10 or higher
- Jupyter Notebook or Google Colab, optional
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`

Additional packages such as `wfdb`, `pydicom`, `SimpleITK`, `PyTorch`, `FAISS`, or `Chroma` may be used in advanced classes, but they are not required for the basic version of this repository.

---

## For students

<details>
<summary><b>What to describe in your assignment</b> (click to expand)</summary>
<br>

- what data were used;
- what the code calculated or visualized;
- what the output means;
- what limitations the method has;
- why the result cannot be treated as a clinical conclusion.

</details>

---

## For instructors

<details>
<summary><b>Pre-class checklist</b> (click to expand)</summary>
<br>

Before class, it is recommended to:

- check that all scripts run from the repository root;
- verify that file paths to `data/` are correct;
- prepare Jupyter or Google Colab versions if needed;
- explain that synthetic data are used for training purposes;
- evaluate both technical execution and clinical interpretation.

</details>

<details>
<summary><b>Suggested assessment structure</b> (click to expand)</summary>
<br>

| Criterion | Weight |
|---|---:|
| Code execution | 20% |
| Understanding of data structure | 20% |
| Interpretation of metrics or plots | 25% |
| Clinical meaning of the conclusion | 25% |
| Clarity and accuracy of the report | 10% |

</details>

---

## License and citation

This repository is intended for educational use.  
If you use or adapt these materials in teaching, please cite the accompanying textbook or teaching course where appropriate.

---

<div align="center">

**Digital medicine requires not only intelligent algorithms, but also clinically responsible interpretation.**

</div>
