from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from memory.shared_memory import SharedMemory

def main(file_path):
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)
    json_agent = JSONAgent()
    email_agent = EmailAgent()

    format_, intent = classifier.classify(file_path)

    if format_ == "JSON":
        result = json_agent.process(file_path, memory)
    elif format_ == "Email":
        result = email_agent.process(file_path, memory)
    else:
        result = "PDF processing not implemented yet."

    print("Processing Result:", result)

if __name__ == "__main__":
    # Change this path to test different files
    main("inputs/sample_email.txt")
