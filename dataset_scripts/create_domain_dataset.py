import pandas as pd


data = [

    # =========================
    # FINANCIAL COMPLAINTS
    # =========================

    ("Someone used my credit card without my permission", "Financial"),
    ("My bank account was charged incorrectly", "Financial"),
    ("I found an unauthorized transaction", "Financial"),
    ("My credit card payment was declined", "Financial"),
    ("There is a problem with my bank account", "Financial"),
    ("I was charged a wrong amount on my credit card", "Financial"),
    ("My loan payment is showing incorrectly", "Financial"),
    ("I want to dispute a transaction", "Financial"),
    ("My bank transfer has not gone through", "Financial"),
    ("Someone stole money from my account", "Financial"),
    ("I do not recognize this transaction", "Financial"),
    ("My credit report contains incorrect information", "Financial"),
    ("I have an issue with my credit card", "Financial"),
    ("My bank account has an unauthorized withdrawal", "Financial"),
    ("I was charged twice for the same transaction", "Financial"),
    ("My loan account information is incorrect", "Financial"),
    ("I need help with my credit report", "Financial"),
    ("My card was declined during payment", "Financial"),
    ("There is a fraudulent transaction on my account", "Financial"),
    ("My bank charged me an unexpected fee", "Financial"),
    ("I cannot access my bank account", "Financial"),
    ("My credit card was used by someone else", "Financial"),
    ("I have a problem with my loan", "Financial"),
    ("My account balance is incorrect", "Financial"),
    ("I want to report a suspicious transaction", "Financial"),
    ("My payment was processed incorrectly", "Financial"),
    ("I received a wrong bill from the bank", "Financial"),
    ("My credit card has an incorrect charge", "Financial"),
    ("I am having trouble with a bank transfer", "Financial"),
    ("There is an error in my credit report", "Financial"),
    ("My loan payment was charged twice", "Financial"),
    ("I lost money because of an unauthorized transaction", "Financial"),
    ("My bank account transaction is not mine", "Financial"),
    ("I need to dispute a credit card charge", "Financial"),
    ("My card transaction was declined", "Financial"),
    ("The bank deducted money incorrectly", "Financial"),
    ("I have a dispute regarding my bank transaction", "Financial"),
    ("Someone hacked my bank account", "Financial"),
    ("My credit card information was stolen", "Financial"),
    ("I need help resolving a banking issue", "Financial"),

    # =========================
    # COMPANY COMPLAINTS
    # =========================

    ("My salary has not been credited", "Company"),
    ("My attendance was marked incorrectly", "Company"),
    ("I am unable to login to my company account", "Company"),
    ("I need to apply for leave", "Company"),
    ("My laptop is not working", "Company"),
    ("I have a problem with HR", "Company"),
    ("The office AC is not working", "Company"),
    ("The company software is not working", "Company"),
    ("My salary is incorrect", "Company"),
    ("I cannot access the employee portal", "Company"),
    ("My attendance is missing", "Company"),
    ("I want to know my leave balance", "Company"),
    ("My office laptop has stopped working", "Company"),
    ("I need to contact HR regarding an issue", "Company"),
    ("The office internet is not working", "Company"),
    ("I cannot login to the employee system", "Company"),
    ("My salary payment is delayed", "Company"),
    ("I was marked absent incorrectly", "Company"),
    ("I need approval for my leave", "Company"),
    ("My work computer is not working", "Company"),
    ("I need help from the HR department", "Company"),
    ("The office air conditioner is broken", "Company"),
    ("The internal software has an error", "Company"),
    ("My payroll information is incorrect", "Company"),
    ("My employee account is locked", "Company"),
    ("My attendance record needs correction", "Company"),
    ("I want to take leave next week", "Company"),
    ("My desktop computer is not working", "Company"),
    ("I have an issue with my HR records", "Company"),
    ("The office network is down", "Company"),
    ("I forgot my company login password", "Company"),
    ("My salary has been calculated incorrectly", "Company"),
    ("I was absent but the system shows present", "Company"),
    ("My leave request is not showing", "Company"),
    ("The company laptop has a technical problem", "Company"),
    ("I need assistance with an HR issue", "Company"),
    ("The office printer is not working", "Company"),
    ("The company application is showing an error", "Company"),
    ("My employee portal is not accessible", "Company"),
    ("There is a problem with my payroll", "Company"),
]


df = pd.DataFrame(data, columns=["complaint", "domain"])

df.to_csv("../data/domain_complaints.csv", index=False)

print("Domain dataset created successfully!")
print("Total complaints:", len(df))

print("\nDomain distribution:")
print(df["domain"].value_counts())

print("\nDataset preview:")
print(df.head())
