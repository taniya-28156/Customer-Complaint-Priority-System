from ml_utils import predict_domain, predict_category, predict_priority


complaints = [
    "Someone used my credit card without my permission",
    "My salary has not been credited",
    "My attendance was marked incorrectly",
    "I cannot login to my employee portal",
    "My bank account has an unauthorized transaction",
    "I need to apply for leave",
    "My office laptop is not working",
    "My credit card payment was declined"
]


for complaint in complaints:

    domain = predict_domain(complaint)
    category = predict_category(complaint)
    priority = predict_priority(complaint)

    print("Complaint:", complaint)
    print("Domain:", domain)
    print("Category:", category)
    print("Priority:", priority)
    print("-" * 60)