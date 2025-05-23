Problem Statement:
You are tasked with building a lightweight AI agent that can intelligently answer basic questions from a simple CSV file containing customer purchase data or any client data.

The agent should be able to:

Parse the CSV file.

Understand simple user queries in natural language.


Working Principle:

Parsing: 
Using of the python's CSV Module to read the csv data and store the headers and data

Language Model:
Using of a local model from transformers pipeline like gpt-2 to use user query and the csv file to generate a reponse

User queries:
User can ask queries like "Top 5 customers with the most purchases?"


To run the project:

1. Install required packages
pip install transformers torch

2. Collect CSV data

3. Run the project
python run agent.py
