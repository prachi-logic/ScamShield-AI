# 🛡️ ScamShield AI

### AI-Powered SMS Scam & Spam Detection System

ScamShield AI is a machine learning-based system that analyzes SMS messages and detects whether they are legitimate or suspicious.

## 🚀 Features

- 📩 SMS Spam Detection
- 🔤 TF-IDF Text Vectorization
- 🤖 Machine Learning Model Comparison
- 🎯 Final SVM-based Classification
- ⚠️ Scam Risk Assessment
- 🚩 Red Flag Detection
- 🏷️ Scam Type Detection
- 📊 Confusion Matrix & Model Evaluation

## 🧠 Machine Learning Models

The project compares three machine learning algorithms:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (SVM)

The final system uses a calibrated Linear SVM for prediction and risk assessment.

## 🔄 Project Workflow

SMS Message  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Machine Learning Model  
↓  
Spam Probability  
↓  
Red Flag Detection  
↓  
Scam Type Detection  
↓  
Final Risk Level

## 📊 Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🛡️ Risk Levels

The system categorizes messages into:

- LOW RISK
- MEDIUM RISK
- HIGH RISK

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Google Colab
- Jupyter Notebook

## 📁 Project Files

- `ScamShield_AI.ipynb` — Complete ML notebook
- `scamshield_svm_model.pkl` — Trained SVM model
- `tfidf_vectorizer.pkl` — TF-IDF vectorizer

## 👩‍💻 Project

ScamShield AI is developed as a machine learning project for detecting suspicious SMS messages and demonstrating an end-to-end ML workflow.
