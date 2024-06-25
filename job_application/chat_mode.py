import os
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = handle_user_input(user_input)
    return jsonify(response)

def handle_user_input(user_input):
    if 'resume' in user_input.lower():
        return {"message": "Do you have a resume to upload?"}
    elif 'linkedin' in user_input.lower():
        return {"message": "Please provide your LinkedIn profile URL."}
    elif 'salary' in user_input.lower():
        return {"message": "What are your salary expectations?"}
    else:
        return {"message": "I'm here to help you with your job search. How can I assist you today?"}

if __name__ == '__main__':
    app.run(debug=True)
