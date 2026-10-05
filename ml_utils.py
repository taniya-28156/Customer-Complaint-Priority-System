import joblib

# Load trained model and vectorizer
# Financial model
model = joblib.load("models/logistic_regression_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Company model
company_model = joblib.load("models/company_category_model.pkl")
company_vectorizer = joblib.load("models/company_tfidf_vectorizer.pkl")

# Domain model
domain_model = joblib.load("models/domain_model.pkl")
domain_vectorizer = joblib.load("models/domain_tfidf_vectorizer.pkl")


def predict_category(complaint):
    """
    Predict complaint category based on complaint domain.
    """

    domain = predict_domain(complaint)

    # Financial complaint
    if domain == "Financial":
        complaint_vector = vectorizer.transform([complaint])
        prediction = model.predict(complaint_vector)
        return prediction[0]

    # Company complaint
    elif domain == "Company":
        complaint_vector = company_vectorizer.transform([complaint])
        prediction = company_model.predict(complaint_vector)
        return prediction[0]

def predict_category_confidence(complaint):

    domain = predict_domain(complaint)

    if domain == "Financial":

        complaint_vector = vectorizer.transform([complaint])

        probabilities = model.predict_proba(complaint_vector)

        confidence = probabilities.max()

        return round(confidence * 100, 2)

    elif domain == "Company":

        complaint_vector = company_vectorizer.transform([complaint])

        probabilities = company_model.predict_proba(complaint_vector)

        confidence = probabilities.max()

        return round(confidence * 100, 2)
    
def predict_domain(complaint):
    complaint_vector = domain_vectorizer.transform([complaint])
    prediction = domain_model.predict(complaint_vector)

    return prediction[0]


def predict_priority(complaint):
    complaint = complaint.lower()

    # =========================
    # HIGH PRIORITY
    # =========================

    high_keywords = [
        # Financial
        "fraud",
        "stolen",
        "steal",
        "stole",
        "unauthorized",
        "unauthorised",
        "hack",
        "hacked",
        "scam",
        "identity theft",
        "lost money",
        "money stolen",
        "credit card used",
        "card used",
        "without permission",
        "without authorization",
        "without my consent",
        "without my permission",

        # Company
        "salary not credited",
        "salary has not been credited",
        "salary not received",
        "salary delayed",
        "server is down",
        "production is down",
        "system is down",
        "cannot work",
        "security breach",
        "account hacked",
        "urgent",
        "critical"
    ]

    # =========================
    # MEDIUM PRIORITY
    # =========================

    medium_keywords = [
        # Financial
        "delay",
        "late",
        "incorrect",
        "error",
        "dispute",
        "declined",
        "charged twice",

        # Company
        "attendance",
        "leave",
        "login",
        "laptop",
        "internet",
        "software",
        "technical",
        "hr",
        "salary",
        "problem",
        "issue"
    ]

    # Check High first
    for word in high_keywords:
        if word in complaint:
            return "🔴 High"

    # Check Medium second
    for word in medium_keywords:
        if word in complaint:
            return "🟡 Medium"

    # Otherwise Low
    return "🟢 Low"