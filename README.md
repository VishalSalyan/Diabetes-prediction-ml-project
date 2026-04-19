# 🩺 Diabetes Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-KNN%20%7C%20LogReg%20%7C%20RF-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A **machine learning classification project** that predicts whether a person is diabetic based on medical diagnostic features. The project compares multiple ML models and deploys the best-performing model using a **Streamlit web application** for real-time predictions.

---

## 📌 Project Overview

This project focuses on building an end-to-end ML pipeline:

- Data preprocessing & feature scaling
- Training multiple classification models
- Model evaluation using multiple metrics
- Performance comparison
- Deployment using Streamlit

The goal is to assist in early diabetes detection using machine learning.

---

## 📊 Dataset

- **Dataset:** Pima Indians Diabetes Dataset
- **Type:** Binary Classification
- **Target:** Diabetes (0 = No, 1 = Yes)

### 🔹 Features:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## 🧠 Machine Learning Models Used

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Random Forest Classifier

---

## 📈 Model Performance Comparison

| Model               | Accuracy | Recall | F1 Score |
| ------------------- | -------- | ------ | -------- |
| KNN                 | 0.76     | 0.53   | 0.61     |
| Logistic Regression | 0.75     | 0.67   | 0.66     |
| Random Forest       | 0.75     | 0.60   | 0.63     |

---

## 🏆 Best Model Insight

- KNN achieved the highest accuracy
- Logistic Regression performed best overall due to:
  - Higher recall (important for medical prediction)
  - Better balance between precision and recall

👉 In medical use cases, recall is more important than accuracy.

---

## 🚀 Streamlit Web App

An interactive web application allows users to input health parameters and get real-time diabetes predictions.

### ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
diabetes-prediction/
│
├── app.py
├── model/
│   ├── trained_model.sav
│   └── scaler.sav
│
├── data/
│   └── diabetes.csv
│
├── notebooks/
│   └── notebook.ipynb
│
├── src/
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit

---

## 🔍 Key Features

- End-to-end ML pipeline
- Data preprocessing & scaling
- Multiple model comparison
- Evaluation using Accuracy, Recall & F1-score
- Interactive Streamlit dashboard
- Real-time prediction system

---

## 📌 Future Improvements

- Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
- Handling class imbalance (SMOTE)
- Cloud deployment (Streamlit Cloud / Render)
- Add probability-based risk score
- Improve UI/UX dashboard

---

## 🧑‍💻 Author

**Vishal Salyan**

- Data Science Enthusiast
- Machine Learning & AI Projects Builder

---

## ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🔗 Share it
- 🚀 Connect on GitHub/LinkedIn

---

## 💡 Why this project stands out

- Clean ML pipeline structure
- Real-world medical use case
- Model comparison with proper metrics
- Deployed interactive app
- Recruiter-ready documentation
