import json

class JSONAgent:
    def process(self, file_path, memory):
        with open(file_path) as f:
            data = json.load(f)

        required_fields = ["invoice_id", "amount", "date"]
        missing = [field for field in required_fields if field not in data]

        formatted = {
            "invoice_id": data.get("invoice_id"),
            "amount": data.get("amount"),
            "date": data.get("date"),
            "status": "missing fields: " + ", ".join(missing) if missing else "complete"
        }

        memory.log(file_path, "JSON", "Invoice", json.dumps(formatted))
        return formatted
