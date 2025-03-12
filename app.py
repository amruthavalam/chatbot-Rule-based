import re
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    patterns = {
        r'hi|hello|hey': "Hello! How can I assist you today?",
        r'how are you': "I'm just a bot, but I'm doing great! How about you?",
        r'what is your name': "I'm a simple chatbot created to help you!",
        r'bye|goodbye': "Goodbye! Have a great day!",
        r'how can you help me': "I can answer simple questions and have basic conversations!",
        r'(weather|temperature)': "I can't check the weather, but you can use a weather app!",
        r'who created you': "I was created by a developer learning about chatbots!",
        r'thank you|thanks': "You're welcome! Happy to help!",
        r'help': "Sure! Just ask me anything, and I'll try my best to respond!",
    }
    
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    
    return "I'm sorry, I don't understand that. Can you rephrase?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)