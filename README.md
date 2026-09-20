# 🛡️ ScamShield AI

### AI-Powered SMS Scam & Spam Detection System

ScamShield AI is a machine learning-based system that analyzes SMS messages and detects whether they are legitimate or suspicious.

## 🚀 Live Demo

🔗 **Live App:**  
PASTE-YOUR-STREAMLIT-LINK-HERE

## ✨ Features

- 📩 SMS Spam Detection
- 🔤 TF-IDF Text Vectorization
- 🤖 Machine Learning Model Comparison
- 🎯 Final SVM-based Classification
- 📊 Spam Probability Prediction
- ⚠️ Scam Risk Assessment
- 🚩 Red Flag Detection
- 🏷️ Scam Type Detection
- 📈 Confusion Matrix & Model Evaluation
- 🌐 Streamlit Web Deployment

## 🧠 Machine Learning Models

The project compares three machine learning algorithms:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (SVM)

The final system uses a calibrated Linear SVM for prediction and risk assessment.

## 🔄 Project Workflow

```text
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

📊 Model Evaluation

The models are evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
🛡️ Risk Levels

The system categorizes messages into:

🟢 LOW RISK
🟡 MEDIUM RISK
🔴 HIGH RISK

Risk assessment is based on the model's spam probability and detected red flags.

🏷️ Scam Types

The system identifies common suspicious patterns such as:

OTP / Financial Scam
Prize / Reward Scam
Suspicious Link Scam
Urgency-Based Scam
General Spam
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Streamlit
Joblib
Google Colab
Jupyter Notebook
📁 Project Structure
ScamShield-AI/
│
├── ScamShield_AI.ipynb
├── app.py
├── scamshield_svm_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md
📂 Project Files
ScamShield_AI.ipynb — Complete machine learning notebook
app.py — Streamlit web application
scamshield_svm_model.pkl — Trained calibrated SVM model
tfidf_vectorizer.pkl — Saved TF-IDF vectorizer
requirements.txt — Required Python dependencies
▶️ Run Locally

Clone the repository and install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py
🎯 Project Objective

The objective of ScamShield AI is to demonstrate an end-to-end machine learning workflow for SMS scam and spam detection, from data preprocessing and model training to evaluation and real-world web deployment.

👩‍💻 Project

ScamShield AI

Machine Learning Project built using Python, Scikit-learn and Streamlit.
