from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get('OPENAI_API_KEY')

@app.route('/')
def home():
    return "AI Bot is working!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data['message']
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Roblox bot. Keep answers short."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=30
        )
        
        return jsonify({"response": response.choices[0].message.content})
        
    except Exception as e:
        return jsonify({"response": "Sorry, I'm having trouble!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
