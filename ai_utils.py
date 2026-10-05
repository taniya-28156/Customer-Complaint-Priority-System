import os
print("===== NEW AI_UTILS FILE LOADED =====")
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_response(complaint, domain, category, priority):
    if domain =="Financial":
        role = "You are an AI Financial Customer Support Assistant."
        organization = "bank or financial institution"
    else:
        role = "You are an AI Employee Support Assistant."
        organization = "company or HR support team"

    prompt = f"""
{role}
Analyze the complaint and generate both an internal analysis and a professional customer/employee reply.

Customer Complaint:
{complaint}

Complaint Domain:
{domain}

Predicted Category:
{category}

Predicted Priority:
{priority}

Important Instructions: 
- Use the complaint domain to understand the context.
- Do not mix financial and company-related terminology. 
- For Financial complaints, use appropriate banking/financial terminology. 
- For Company complaints, use appropriate employee/HR/IT/workplace terminology. 
- Do not invent specific policies, amounts, dates, or guarantees. 
- Keep the response concise, professional, and empathetic.

Provide response in this format:

## AI Analysis

Summary:
(write 2-3 lines)

Reason:
(explain why this priority is appropriate)

Suggested Action:
(list practical actions for the {organization} support team)

## Customer Reply

(write a professional and empathetic reply to the customer)

Keep everything concise and professional.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)

        return """
## 🤖 AI Analysis

⚠ AI service is temporarily unavailable.

Summary:
The complaint has been successfully received and recorded.

Reason:
The AI analysis service is currently unavailable. However, the complaint has been processed using the Machine Learning model.

Suggested Action:
- Review the complaint manually.
- Assign it to the appropriate support team.
- Contact the customer if additional information is required.

---

## 📩 Customer Reply

Dear Customer, 
Thank you for contacting us. 
We have successfully received your complaint and assigned it to our support team. 
Our team will investigate your issue and get back to you as soon as possible. 
We appreciate your patience and understanding. 
Best Regards, 
Customer Support Team 
"""