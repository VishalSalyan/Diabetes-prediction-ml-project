# 🩺 Diabetes Prediction using Machine Learning

A machine learning project that predicts whether a person is diabetic or not based on medical diagnostic features. The project compares multiple models and deploys the best-performing model using a Streamlit web application.

---

## 📌 Project Overview

This project uses machine learning algorithms to analyze patient health data and predict the likelihood of diabetes. Multiple models were trained and evaluated, and performance was compared using accuracy, recall, and F1-score.

The final model is deployed as an interactive **Streamlit web app**.

---

## 📊 Dataset

- Source: Pima Indians Diabetes Dataset
- Features:
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
- Random Forest

---

## 📈 Model Performance Comparison

| Model               | Accuracy | Recall | F1 Score |
| ------------------- | -------- | ------ | -------- |
| KNN                 | 0.76     | 0.53   | 0.61     |
| Logistic Regression | 0.75     | 0.67   | 0.66     |
| Random Forest       | 0.75     | 0.60   | 0.63     |

### 🏆 Best Model

Although KNN achieved the highest accuracy, **Logistic Regression performed best overall** due to higher recall and balanced F1-score, making it more reliable for medical prediction.

---

## 🚀 Web App (Streamlit)

The trained model is deployed using Streamlit to provide a simple and interactive user interface for real-time predictions.

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
├── app.py                  # Streamlit web app
├── trained_model.sav       # Saved ML model
├── scaler.sav              # Feature scaler
├── notebook.ipynb          # Model training notebook
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Technologies Used

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit

---

## 🔍 Key Features

- Data preprocessing and feature scaling
- Model comparison (KNN, Logistic Regression, Random Forest)
- Evaluation using accuracy, recall, and F1-score
- Interactive Streamlit web app
- Real-time diabetes prediction

---

## 📌 Future Improvements

- Hyperparameter tuning for better performance
- Handling class imbalance for better recall
- Deployment on cloud (Streamlit Cloud / Render)
- Adding probability score for predictions

---

## 🧑‍💻 Author

**Vishal Salyan**

- Data Science Enthusiast
- Interested in Machine Learning & AI Applications

---

## ⭐ If you like this project

Feel free to ⭐ star this repository and connect!
