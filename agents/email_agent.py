class EmailAgent:
    def process(self, file_path, memory):
        with open(file_path) as f:
            content = f.read()

        sender = "unknown@example.com"
        urgency = "High" if "urgent" in content.lower() else "Normal"
        intent = "RFQ" if "quote" in content.lower() else "General"

        output = {
            "sender": sender,
            "urgency": urgency,
            "intent": intent,
            "formatted": f"From: {sender}\nUrgency: {urgency}\nContent: {content[:100]}"
        }

        memory.log(file_path, "Email", intent, str(output))
        return output
