import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 🚀 Feature extraction from URL
def extract_features(url):
    return {
        "url_length": len(url),
        "has_https": int("https" in url.lower()),
        "count_dots": url.count('.'),
        "count_hyphens": url.count('-'),
        "count_at": url.count('@'),
        "suspicious_word": int(any(word in url.lower() for word in ['secure', 'account', 'update', 'login', 'verify', 'paypal', 'signin']))
    }

# 📥 Load the dataset
df = pd.read_csv("data/phishing_dataset.csv")

# ⚙️ Extract features into a DataFrame
features = df['url'].apply(extract_features).apply(pd.Series)
labels = df['label']

# 📊 Train the model
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Save model and feature list
model_dir = "phishing_detector/model"
os.makedirs(model_dir, exist_ok=True)

with open(f"{model_dir}/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open(f"{model_dir}/features_list.pkl", "wb") as f:
    pickle.dump(list(features.columns), f)

print("✅ Model trained with advanced features and saved!")

