# 🔐 Customer Risk Classification Model

A mini Machine Learning project that predicts customer risk levels as **Low, Medium, or High** using customer and transaction-related data.

This project covers the complete Machine Learning workflow, including data cleaning, feature engineering, visualization, model training, and evaluation.

---

## 📌 Project Overview

The goal of this project is to build a classification model that predicts a customer's risk level based on different customer and transaction-related factors.

The model uses:

- Customer age
- Country risk
- Transaction count
- Transaction value
- Account age
- Failed login attempts

The target variable is `risk_label`, which contains three classes:

- **Low**
- **Medium**
- **High**

---

## 🗂️ Dataset

The dataset contains the following columns:

| Column | Description |
|---|---|
| `customer_age` | Age of the customer |
| `country_risk` | Risk level associated with the customer's country |
| `transaction_count` | Number of transactions |
| `transaction_value` | Value of transactions |
| `account_age` | Age of the customer's account |
| `failed_logins` | Number of failed login attempts |
| `risk_label` | Customer's risk category |

The original CSV data has **2 categorical columns** (`country_risk` and `risk_label`), while the remaining columns are numerical.

---

## 🧹 Data Preprocessing

Several preprocessing steps were performed before training the model.

### 1. Removing Duplicate Data

Duplicate records were removed from the dataset to avoid repeated data affecting the model.

### 2. Correcting Inconsistent Values

Inconsistent values in the `country_risk` column were standardized.

For example:

- `Low` → `low`
- `LOW` → `low`
- `Medium` → `medium`
- `MEDIUM` → `medium`
- `High` → `high`
- `HIGH` → `high`
- ` High` → `high`

### 3. Handling Missing Values

Missing values were handled using different methods depending on the column:

- `customer_age` → Mean
- `transaction_value` → Median
- `account_age` → Mean
- `country_risk` → Mode

### 4. Feature Engineering

A new feature called `transaction_frequency` was created using `transaction_count`.

Customers were grouped into:

- Low
- Medium
- High

based on their transaction count.

### 5. Encoding Categorical Data

Categorical features were converted into numerical form using:

- **One-hot encoding** for input features
- **Label encoding** for the target variable

---

## 🤖 Machine Learning Model

A **Random Forest Classifier** was used to predict customer risk levels.

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The model was trained using the training data and evaluated using the test data.

The Random Forest model was created using a fixed `random_state=42` to make the results reproducible.

---

## 📊 Model Evaluation

The model was evaluated using the following metrics:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix**

### Model Performance

The Random Forest model achieved:

**Accuracy: 62%**

This means the model correctly predicted the risk category for approximately 62% of the test samples.

---

## 📈 Visualizations

The project includes several visualizations to understand the data and model results.

### Risk Label Distribution

Shows the number of customers belonging to each risk category.

### Average Failed Logins by Risk Level

Compares the average number of failed login attempts for Low, Medium, and High-risk customers.

### Average Transaction Value by Risk Level

Compares the average transaction value across different risk categories.

### Confusion Matrix

Shows the model's correct and incorrect predictions for each risk category.

---

## 🔎 Key Findings

1. The original CSV data has **2 categorical columns**, while the remaining columns are numerical.

2. I used a **Random Forest Classifier**, which achieved **62% accuracy** on the test data.

3. **Low-risk customers had the highest average failed logins**, with an average of 1.88.

4. **Medium-risk customers had the highest average transaction value**, with an average of 309.63.

5. The risk categories were fairly balanced, with **221 High-risk, 215 Low-risk, and 214 Medium-risk customers**.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** — Data loading, cleaning, and manipulation
- **Scikit-learn** — Machine learning, preprocessing, and model evaluation
- **Matplotlib** — Data visualization
- **Jupyter Notebook** — Project development and documentation

---

## 📁 Project Structure

Customer-Risk-Classification/
│
├── customer_risk_data.csv
├── customer_risk_data_cleaned.csv
├── risk_classification.ipynb
├── main.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1. Clone the repository

Replace `<your-repository-link>` with your GitHub repository link.

`git clone <your-repository-link>`

### 2. Navigate to the project folder

`cd Customer-Risk-Classification`

### 3. Install the required libraries

`pip install -r requirements.txt`

### 4. Run the project

The project can be run using either:

- `main.py`
- `risk_classification.ipynb`

---

## 🎯 Conclusion

This project demonstrates a complete Machine Learning workflow, from **data preprocessing and feature engineering to visualization, model training, and evaluation**.

The Random Forest Classifier achieved **62% accuracy** on the test data and was used to classify customers into Low, Medium, and High-risk categories.

The project also provided useful insights into customer transaction behavior, failed login attempts, and the distribution of different risk levels.

Future improvements could include testing other classification algorithms, tuning the Random Forest parameters, and adding more relevant features to improve model performance.

---

## 👩‍💻 Project Purpose

This project was completed as a **Day 10 Mini ML Project** to independently apply Machine Learning concepts to a real-world-style classification problem.