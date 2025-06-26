# 🌼 Task 3 – End-to-End Data Science Project: Iris Flower Prediction Web App

This repository contains Task 3 of my Data Science Internship at CODTECH:  
An end-to-end machine learning project where I trained an ML model to classify Iris flowers, and deployed it using a **Flask web application**.

---

## ✅ Objective

Build a complete Data Science pipeline from data loading, preprocessing, model training, and finally deploying it as a simple **web interface using Flask**.

---

## 🧪 Tools & Technologies

- Python
- scikit-learn
- joblib
- NumPy
- Flask
- HTML/CSS (Jinja2 templates)

---

## 📊 Dataset

- **Source**: [`sklearn.datasets.load_iris()`](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
- **Features**:
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- **Target**:
  - 0: Setosa
  - 1: Versicolor
  - 2: Virginica

---

## 🧠 ML Model

- **Model**: Support Vector Machine (SVM)
- **Accuracy**: ~95% on test data
- **Saved as**: `model.pkl` using `joblib`

---

## 🧰 Folder Structure

Task 3 - End-to-End Project/
├── model.pkl # Trained model file
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend form
├── README.md # You’re reading this :)

---

## 🌐 How the Web App Works

1. User inputs 4 flower measurements on the form
2. The data is passed to the Flask backend via a POST request
3. The pre-trained model (`model.pkl`) predicts the class (Setosa, Versicolor, Virginica)
4. The result is shown on the same page

---

## 🚀 How to Run the App

1. Clone this repository or open it in your system
2. Make sure Python is installed
3. Install Flask (if not already):
```bash
pip install flask joblib numpy scikit-learn

| Sepal Length | Sepal Width | Petal Length | Petal Width | Species    |
| ------------ | ----------- | ------------ | ----------- | ---------- |
| 5.1          | 3.5         | 1.4          | 0.2         | Setosa     |
| 6.0          | 2.9         | 4.5          | 1.5         | Versicolor |
| 6.3          | 3.3         | 6.0          | 2.5         | Virginica  |
