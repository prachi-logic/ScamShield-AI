# 🛡️ ScamShield AI

### AI-Powered SMS Scam & Spam Detection System

ScamShield AI is a machine learning-based system that analyzes SMS messages and detects whether they are legitimate or suspicious.

---

## 🚀 Live Demo

🔗 **Live App:**  https://scamshield-aigit-ynry5wma6qvdvycou72lwx.streamlit.app/

---

## ✨ Features

- 📩 SMS Spam Detection
- 🔤 TF-IDF Text Vectorization
- 🤖 Machine Learning Model Comparison
- 🎯 Final SVM-Based Classification
- 📊 Spam Probability Prediction
- ⚠️ Scam Risk Assessment
- 🚩 Red Flag Detection
- 🏷️ Scam Type Detection
- 📈 Confusion Matrix & Model Evaluation
- 🌐 Streamlit Web Deployment

---

## 🧠 Machine Learning Models

The project compares three machine learning algorithms:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (SVM)

The final system uses a calibrated Linear SVM for prediction and risk assessment.

---

## 🔄 Project Workflow

SMS Message  
↓  
Text Preprocessing  
↓  
TF-IDF Vectorization  
↓  
Machine Learning Models  
↓  
Final SVM Prediction  
↓  
Spam Probability  
↓  
Red Flag Detection  
↓  
Scam Type Detection  
↓  
Final Risk Level

---

## 📊 Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🛡️ Risk Levels

The system categorizes messages into:

- 🟢 **LOW RISK**
- 🟡 **MEDIUM RISK**
- 🔴 **HIGH RISK**

Risk assessment is based on the model's spam probability and detected red flags.

---

## 🏷️ Scam Types

The system identifies common suspicious patterns such as:

- OTP / Financial Scam
- Prize / Reward Scam
- Suspicious Link Scam
- Urgency-Based Scam
- General Spam

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib
- Google Colab
- Jupyter Notebook

---

## 📁 Project Structure

```text
ScamShield-AI/
│
├── ScamShield_AI.ipynb
├── app.py
├── scamshield_svm_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
