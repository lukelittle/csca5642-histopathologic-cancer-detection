# Histopathologic Cancer Detection

This project focuses on developing models to identify metastatic cancer in small image patches taken from larger digital pathology scans.

## Project Overview

The goal of this project is to create an algorithm that can accurately classify histopathologic images into two categories:
1. Images containing metastatic cancer tissue
2. Images containing normal tissue (no cancer)

This is part of the Kaggle competition for Histopathologic Cancer Detection.

## Dataset

The dataset is a slightly modified version of the PatchCamelyon (PCam) benchmark dataset. The original PCam dataset contains duplicate images due to its probabilistic sampling, but the version presented on Kaggle does not contain duplicates.

PCam is notable for:
- Its size and approachability
- Simplicity to get started on
- Packing a clinically-relevant task (metastasis detection) into a straightforward binary image classification task
- Models can be trained on a single GPU in a couple of hours
- The balance between task-difficulty and tractability makes it suitable for fundamental machine learning research on topics like active learning, model uncertainty, and explainability

Each image in the dataset is a 96x96 pixel RGB image, and the task is to determine whether the center 32x32px region contains at least one pixel of tumor tissue.

## Repository Structure

```
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks
│   ├── 01_Problem_and_Data_Description.ipynb  # Problem statement and data description
│   ├── 02_Exploratory_Data_Analysis.ipynb     # EDA and data preprocessing
│   ├── 03_Model_Architecture.ipynb            # Model architecture design
│   ├── 04_Results_And_Analysis.ipynb          # Results and analysis
│   └── 05_Conclusions.ipynb                   # Conclusion and future work
├── models/                # Saved model files (not tracked by git)
├── docs/                  # Documentation files
├── scripts/               # Utility scripts
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Notebooks

The project is organized into 5 main notebooks:

1. **Problem and Data Description**: Introduction to the problem and dataset exploration.
2. **Exploratory Data Analysis**: Data visualization, cleaning, and preprocessing.
3. **Model Architecture**: Design and implementation of various neural network architectures.
4. **Results and Analysis**: Model training, evaluation, and comparison.
5. **Conclusions**: Summary of findings and potential improvements.

## Evaluation

Submissions are evaluated on the area under the ROC curve (AUC-ROC) between the predicted probability and the observed target. This metric is particularly suitable for binary classification problems, especially when dealing with medical diagnoses.