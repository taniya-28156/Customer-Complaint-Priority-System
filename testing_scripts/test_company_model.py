import joblib

# Load model and vectorizer
model = joblib.load("../models/company_category_model.pkl")
vectorizer = joblib.load("../models/company_tfidf_vectorizer.pkl")


complaints = [
    "My salary has not been credited",
    "I am unable to login to my company account",
    "My attendance was marked incorrectly",
    "I need to apply for leave",
    "My laptop is not working",
    "I have a problem with HR",
    "The office AC is not working properly",
    "I am facing an issue with the company software"
]


for complaint in complaints:

    complaint_vector = vectorizer.transform([complaint])

    prediction = model.predict(complaint_vector)

    print("Complaint:", complaint)
    print("Predicted Category:", prediction[0])
    print("-" * 50)
