from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time
import webbrowser
import threading
from chatbot import chat

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests from frontend

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        ch=chat()
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({'error': 'No prompt provided'}), 400
        
        prompt = data['prompt']
        print(prompt)
        
        # Placeholder for actual AI model processing
        # Replace this with your AI model integration (e.g., Grok, OpenAI, etc.)
        time.sleep(1)  # Simulate processing delay
        response_text = f"Echo: {prompt}"  # Placeholder response
        
        return jsonify({'response': response_text}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def open_browser():
    """Open the default web browser to the Flask app's URL."""
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    # Automatically open the browser after a short delay
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
