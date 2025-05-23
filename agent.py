from transformers import pipeline
import csv

class CSVDataAgent:
    def __init__(self, csv_path, llm=None):
        self.data = []
        self.headers = []
        self.load_csv(csv_path)
        self.llm = pipeline("text-generation", model="gpt2")

    def prompttempt(self, query):
        prompt = (
            "You are query assistant. "
            "Given the set of csv data, answer based on it. "
            f"Use the set of headers (columns: {', '.join(self.headers)}) to query the csv file. "
            f"CSV Data: {', '.join(self.headers)}. "
            f"Question: {query} "
            "Answer:"
        )
        response = self.llm(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text'][len(prompt):].strip()

    def load_csv(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.headers = reader.fieldnames
            self.data = [row for row in reader]

agent = CSVDataAgent("C:\\Users\\sheik\\OneDrive\\Desktop\\aitask\\data\\dress.csv")
while True:
    q = input("Ask a question (or type 'exit'): ")
    if q.strip().lower() == "exit":
        break
    print(agent.prompttempt(q))