import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #fff9fc;
}

h1, h2, h3 {
    color: #6d4c5c;
}

.stButton > button {
    background-color: #d9f2d9;
    color: #2f4f2f;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.result-box {
    padding: 18px;
    border-radius: 15px;
    background-color: #f8d7e3;
    margin-top: 15px;
}

.safe-box {
    padding: 18px;
    border-radius: 15px;
    background-color: #d9f2d9;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Load Trained Model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("scamshield_svm_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer


model, vectorizer = load_model()


# -----------------------------
# Red Flag Detection
# -----------------------------
def get_red_flags(message):

    message = message.lower()
    flags = []

    prize_words = [
        "won", "winner", "prize", "reward",
        "lottery", "congratulations"
    ]

    urgency_words = [
        "urgent", "immediately", "now",
        "hurry", "limited time", "act fast"
    ]

    money_words = [
        "₹", "rs", "rupees", "cash",
        "money", "lakh", "crore"
    ]

    link_words = [
        "click", "link", "http", "www", "verify"
    ]

    personal_words = [
        "password", "otp", "pin",
        "bank", "account", "card"
    ]

    if any(word in message for word in prize_words):
        flags.append("Prize / Reward related")

    if any(word in message for word in urgency_words):
        flags.append("Urgency detected")

    if any(word in message for word in money_words):
        flags.append("Money related")

    if any(word in message for word in link_words):
        flags.append("Suspicious link / verification")

    if any(word in message for word in personal_words):
        flags.append("Personal / financial information")

    return flags


# -----------------------------
# Scam Type Detection
# -----------------------------
def detect_scam_type(message):

    message = message.lower()

    if any(word in message for word in
           ["otp", "password", "pin", "bank", "account", "card"]):
        return "OTP / Financial Scam"

    elif any(word in message for word in
             ["won", "winner", "prize", "reward", "lottery"]):
        return "Prize / Reward Scam"

    elif any(word in message for word in
             ["click", "link", "http", "www", "verify"]):
        return "Suspicious Link Scam"

    elif any(word in message for word in
             ["urgent", "immediately", "hurry", "act fast"]):
        return "Urgency-Based Scam"

    else:
        return "General Spam"


# -----------------------------
# Header
# -----------------------------
st.title("🛡️ ScamShield AI")

st.subheader("AI-Powered SMS Scam & Spam Detection System")

st.write(
    "Enter an SMS message below to analyze its spam probability, "
    "risk level, scam type and suspicious red flags."
)


# -----------------------------
# Message Input
# -----------------------------
message = st.text_area(
    "📩 Enter SMS Message",
    height=150,
    placeholder="Paste an SMS message here..."
)


# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🔍 Analyze Message", use_container_width=True):

    if not message.strip():

        st.warning("Please enter an SMS message.")

    else:

        # TF-IDF transformation
        message_tfidf = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_tfidf)[0]

        # Probability
        probabilities = model.predict_proba(message_tfidf)[0]

        spam_index = list(model.classes_).index("spam")
        spam_probability = probabilities[spam_index] * 100

        # Red flags
        red_flags = get_red_flags(message)

        # Scam type
        scam_type = detect_scam_type(message)

        # Risk level
        if spam_probability >= 70 or len(red_flags) >= 3:
            risk = "HIGH RISK"

        elif spam_probability >= 40 or len(red_flags) >= 2:
            risk = "MEDIUM RISK"

        else:
            risk = "LOW RISK"


        # -----------------------------
        # Results
        # -----------------------------
        st.markdown("## 📊 Analysis Result")

        if prediction == "spam":
            st.error("🚨 Prediction: SPAM")
        else:
            st.success("✅ Prediction: LEGITIMATE")


        st.metric(
            "Spam Probability",
            f"{spam_probability:.2f}%"
        )


        st.write("### 🛡️ Risk Level")

        if risk == "HIGH RISK":
            st.error(risk)

        elif risk == "MEDIUM RISK":
            st.warning(risk)

        else:
            st.success(risk)


        st.write("### 🏷️ Scam Type")
        st.info(scam_type)


        st.write("### 🚩 Red Flags")

        if red_flags:

            for flag in red_flags:
                st.write("🔸", flag)

        else:
            st.success("No major red flags detected.")


        st.markdown("---")

        st.caption(
            "ScamShield AI uses TF-IDF and a calibrated Linear SVM "
            "to classify SMS messages."
        )
