from flask import Flask, request, render_template
from chatbot import chatbot, context  # Import your chatbot and context from chatbot.py

app = Flask(__name__)

# This is the main page where users can chat
@app.route("/", methods=["GET", "POST"])
def chat():
    conversation = []  # To store the conversation history
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.lower() == "stop":
            conversation.append(("You", "stop"))
            conversation.append(("Chatbot", "Bye-bye! Good job!"))
        else:
            answer = chatbot(question=user_input, context=context)
            conversation.append(("You", user_input))
            conversation.append(("Chatbot", answer["answer"]))
    return render_template("chat.html", conversation=conversation)

if __name__ == "__main__":
    app.run(debug=True)