# 🚀 Task 1 – Data Preprocessing & ETL Pipeline | CodTech Data Science Internship

This project is part of my internship with **CodTech IT Solutions**, focusing on creating a complete ETL (Extract, Transform, Load) pipeline using Python libraries such as `pandas` and `scikit-learn`.

---

## 📌 Objective

To automate the data pipeline process, which includes:
- Loading raw data
- Preprocessing (cleaning, encoding, scaling)
- Splitting the dataset
- Exporting cleaned data for modeling

---

## 📂 Dataset Used

**Name:** Iris Flower Dataset  
**Source:** [UCI Repository / Kaggle](https://www.kaggle.com/datasets/uciml/iris)  
**Description:** The Iris dataset contains 150 rows with 5 columns: sepal length, sepal width, petal length, petal width, and species (target class).

---

## 🧪 Steps Performed in the ETL Pipeline

1. **Data Loading:**
   - Imported the dataset using `pandas`.
2. **Data Cleaning:**
   - Checked and handled missing values.
   - Removed unnecessary columns (like `Id`).
3. **Transformation:**
   - Encoded target labels using `LabelEncoder`.
   - Scaled feature values using `StandardScaler`.
4. **Train-Test Split:**
   - Split into training and test sets using `train_test_split()`.
5. **Exporting:**
   - Exported cleaned and processed data to `X_Iris.csv` and `y_Iris.csv`.

---

## 🛠️ Tech Stack & Tools

- **Programming Language:** Python
- **Libraries:** `pandas`, `scikit-learn`, `numpy`
- **Platform:** Visual Studio Code

---

## 📁 Files Included

| File Name           | Description                                |
|---------------------|--------------------------------------------|
| `etl_pipeline.py`   | Python script containing the full ETL code |
| `X_Iris.csv`       | Processed training feature set             |
| `y_Iris.csv`       | Processed training target labels           |
| `Readme.md`         | Documentation of Task 1                    |

---

## ▶️ How to Run

1. Clone this repository or download the folder `Task1_ETL_Pipeline`.
2. Run the `etl_pipeline.py` script using any Python IDE or Google Colab.
3. Make sure `Iris.csv` is in the same directory before running.

---

## ✅ Outcome
Successfully created an automated ETL pipeline that prepares a dataset for modeling by cleaning, encoding, and scaling. The processed data is now ready for machine learning model training.

---

## 🏅 Internship
This task was completed as part of the Data Science Internship offered by CodTech IT Solutions.

---
### This task not only strengthened my skills in data preprocessing and pipeline automation but also laid a strong foundation for building real-world data science solutions. Looking forward to more challenges ahead in this exciting journey!
