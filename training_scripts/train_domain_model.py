import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# 1. Load dataset
df = pd.read_csv("../data/domain_complaints.csv")

print("Dataset loaded successfully!")
print("Total complaints:", len(df))


# 2. Input and output
X = df["complaint"]
y = df["domain"]


# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 4. Convert text into numbers
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# 5. Create model
model = LogisticRegression(max_iter=1000)


# 6. Train model
model.fit(X_train_tfidf, y_train)


# 7. Prediction
y_pred = model.predict(X_test_tfidf)


# 8. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n===== DOMAIN MODEL RESULT =====")
print("Accuracy:", accuracy)


# 9. Classification report
print("\n===== CLASSIFICATION REPORT =====")
print(classification_report(y_test, y_pred))


# 10. Save model
joblib.dump(model, "../models/domain_model.pkl")
joblib.dump(vectorizer, "../models/domain_tfidf_vectorizer.pkl")

print("\nDomain model saved successfully!")
