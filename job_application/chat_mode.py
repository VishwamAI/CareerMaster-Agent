import os
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize session state
def init_session():
    if 'state' not in session:
        session['state'] = 'start'

@app.route('/chat', methods=['POST'])
def chat():
    init_session()
    user_input = request.json.get('message')
    response = handle_user_input(user_input)
    return jsonify(response)

def handle_user_input(user_input):
    state = session.get('state', 'start')

    if state == 'start':
        if 'resume' in user_input.lower():
            session['state'] = 'resume'
            return {"message": "Do you have a resume to upload?"}
        elif 'linkedin' in user_input.lower():
            session['state'] = 'linkedin'
            return {"message": "Please provide your LinkedIn profile URL."}
        elif 'salary' in user_input.lower():
            session['state'] = 'salary'
            return {"message": "What are your salary expectations?"}
        else:
            return {"message": "I'm here to help you with your job search. How can I assist you today?"}

    elif state == 'resume':
        # Handle resume upload logic here
        session['state'] = 'start'
        return {"message": "Thank you for uploading your resume. What are your salary expectations?"}

    elif state == 'linkedin':
        # Handle LinkedIn profile URL logic here
        session['state'] = 'start'
        return {"message": "Thank you for providing your LinkedIn profile. What are your salary expectations?"}

    elif state == 'salary':
        # Handle salary expectations logic here
        session['state'] = 'start'
        return {"message": "Thank you for providing your salary expectations. We will now proceed with the job application process."}

    else:
        session['state'] = 'start'
        return {"message": "I'm here to help you with your job search. How can I assist you today?"}

if __name__ == '__main__':
    app.run(debug=True)
