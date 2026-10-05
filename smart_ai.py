def generate_ai_response(complaint, category, priority):

    # Priority Based Action
    if priority == "🔴 High":
        action = """
• Escalate immediately to the concerned department.
• Contact the customer within 24 hours.
• Investigate the issue on priority.
"""

    elif priority == "🟡 Medium":
        action = """
• Assign the complaint to the appropriate support team.
• Resolve within 2-3 business days.
• Keep the customer updated.
"""

    else:
        action = """
• Review the complaint.
• Resolve during the normal support cycle.
• Inform the customer once resolved.
"""

    reply = f"""
## 🤖 AI Analysis

### Summary
The complaint has been analyzed successfully.

### Category
{category}

### Priority
{priority}

### Reason
This complaint has been classified under **{category}** based on the complaint text.
The assigned priority is **{priority}** considering the severity of the issue.

### Suggested Action
{action}

---

## 📩 Customer Reply

Dear Customer,

Thank you for contacting us.

We have successfully received your complaint regarding **{category}**.

Our support team has started reviewing your request and will contact you as soon as possible.

Thank you for your patience.

Best Regards,
Customer Support Team
"""

    return reply