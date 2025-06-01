import os
import json

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory

    def classify(self, file_path):
        if file_path.endswith('.json'):
            format_ = "JSON"
            with open(file_path) as f:
                data = json.load(f)
                intent = data.get("intent", "Unknown")
        elif file_path.endswith('.pdf'):
            format_ = "PDF"
            intent = "Regulation"  # Default example
        else:
            format_ = "Email"
            with open(file_path) as f:
                data = f.read()
                if "urgent" in data.lower():
                    intent = "Complaint"
                elif "quote" in data.lower():
                    intent = "RFQ"
                else:
                    intent = "General"

        self.memory.log(file_path, format_, intent, extracted_values="N/A")
        return format_, intent
