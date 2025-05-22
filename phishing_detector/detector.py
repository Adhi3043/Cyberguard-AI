import pickle
import os
import pandas as pd  # ✅ Needed to fix the warning

model_path = os.path.join(os.path.dirname(__file__), "model")

# Load model and feature names
with open(os.path.join(model_path, "phishing_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(model_path, "features_list.pkl"), "rb") as f:
    feature_names = pickle.load(f)

# 🚀 Smarter feature extractor
def extract_features(url):
    return {
        "url_length": len(url),
        "has_https": int("https" in url.lower()),
        "count_dots": url.count('.'),
        "count_hyphens": url.count('-'),
        "count_at": url.count('@'),
        "suspicious_word": int(any(word in url.lower() for word in [
            'secure', 'account', 'update', 'login', 'verify', 'paypal', 'signin'
        ]))
    }

# 🔍 Main detector function
def is_phishing_url(url: str) -> dict:
    features = extract_features(url)
    df = pd.DataFrame([features])  # ✅ Makes it compatible with sklearn model input
    prediction = model.predict(df)[0]
    confidence = model.predict_proba(df)[0].max()
    return {
        "url": url,
        "is_phishing": bool(prediction),
        "confidence": round(confidence * 100, 2)
    }

