import joblib

model = joblib.load("../models/logistic_regression_model.pkl")

print("Financial Complaint Categories:")
print("--------------------------------")

for category in model.classes_:
    print(category)

print("\nTotal Categories:", len(model.classes_))
