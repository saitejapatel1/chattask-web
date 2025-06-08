from transformers import pipeline

# Load the question-answering model (our robot brain)
chatbot = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# This is the story our chatbot will use to find answers
context = """
My name is Alex. I am a student at Sunshine College. I love to learn about artificial intelligence.
My favorite subject is computer science, and I am doing an internship where I build a chatbot.
Sunshine College is in California, and it has a big library with 10,000 books.
"""