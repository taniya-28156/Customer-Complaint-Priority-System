import joblib


# Load model
model = joblib.load("models/domain_model.pkl")
vectorizer = joblib.load("models/domain_tfidf_vectorizer.pkl")


complaints = [
    "Someone stole money from my bank account",
    "My credit card payment was declined",
    "I cannot login to my employee portal",
    "My salary has not been credited",
    "My attendance is incorrect",
    "I need to apply for leave",
    "There is an unauthorized transaction on my account",
    "My office laptop is not working"
]


for complaint in complaints:

    complaint_vector = vectorizer.transform([complaint])

    prediction = model.predict(complaint_vector)

    print("Complaint:", complaint)
    print("Predicted Domain:", prediction[0])
    print("-" * 50)