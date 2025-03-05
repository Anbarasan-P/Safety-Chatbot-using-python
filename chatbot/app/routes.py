from flask import Blueprint, render_template, request, jsonify
from .chatbot import get_chatbot_response

# Create a Blueprint for the chatbot
chat_bp = Blueprint('chat', __name__)

# Route for the root URL ("/")
@chat_bp.route('/')
def home():
    # Serve the index.html template
    return render_template('index.html')

# Route for handling chatbot requests ("/chat")
@chat_bp.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the request
    user_input = request.json.get('message')
    
    # Get the chatbot's response
    response = get_chatbot_response(user_input)
    
    # Return the response as JSON
    return jsonify({"response": response})