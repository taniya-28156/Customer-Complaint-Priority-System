import streamlit as st
import pandas as pd
from datetime import datetime
import os
import requests


# -----------------------------
# Save History Function
# -----------------------------
def save_history(complaint, domain, category, priority):

    data = {
        "Complaint": [complaint],
        "Domain": [domain],
        "Category": [category],
        "Priority": [priority],
        "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    df = pd.DataFrame(data)

    file_name = "history.csv"

    if os.path.exists(file_name):
        old_data = pd.read_csv(file_name)
        df = pd.concat([old_data, df], ignore_index=True)

    df.to_csv(file_name, index=False)


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Customer Complaint Priority System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Complaint Priority System")

st.markdown("""
This application uses **Machine Learning + NLP + FastAPI + Gemini AI**
to analyze customer complaints.
""")

st.divider()

# -----------------------------
# Sidebar Dashboard
# -----------------------------
st.sidebar.title("📊 Complaint Dashboard")

if os.path.exists("history.csv"):

    history = pd.read_csv("history.csv")

    st.sidebar.metric(
        "Total Complaints",
        len(history)
    )

    st.sidebar.metric(
        "🔴 High",
        len(history[history["Priority"] == "🔴 High"])
    )

    st.sidebar.metric(
        "🟡 Medium",
        len(history[history["Priority"] == "🟡 Medium"])
    )

    st.sidebar.metric(
        "🟢 Low",
        len(history[history["Priority"] == "🟢 Low"])
    )

else:

    st.sidebar.info("No complaints analyzed yet.")


# -----------------------------
# Complaint Input
# -----------------------------
complaint = st.text_area(
    "📝 Enter Customer Complaint",
    height=200,
    placeholder="Example: Someone used my credit card without authorization..."
)


# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🔍 Analyze Complaint", use_container_width=True):

    if complaint.strip() == "":
        st.warning("Please enter a complaint.")

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={
                    "complaint": complaint
                }
            )

            if response.status_code != 200:
                st.error("FastAPI returned an error.")
                st.code(response.text)
                st.stop()

            result = response.json()

            domain = result["domain"]
            category = result["category"]
            confidence = result["confidence"]
            priority = result["priority"]
            ai_response = result["ai_response"]

            save_history(
                complaint,
                domain,
                category,
                priority
            )

            st.success("Complaint analyzed successfully!")

            # Domain
            st.subheader("📌 Complaint Domain")
            st.info(domain)

            # Category
            st.subheader("📂 Predicted Category")
            st.info(category)

            # Confidence Score
            st.subheader("🎯 Confidence Score")
            st.info(f"{confidence}%")

            # Priority
            st.subheader("🚨 Complaint Priority")

            if priority == "🔴 High":
                st.error(priority)

            elif priority == "🟡 Medium":
                st.warning(priority)

            else:
                st.success(priority)

            # AI Response
            st.subheader("🤖 AI Analysis + Customer Reply")
            st.write(ai_response)

        except Exception as e:

            st.error("Unable to connect to FastAPI Server.")
            st.code(str(e)) 