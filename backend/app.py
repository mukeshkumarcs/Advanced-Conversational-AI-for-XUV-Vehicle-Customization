from flask import Flask, request, jsonify
from nlp_processing import process_user_input
from user_management import create_user, update_user_preference
from data_analysis import generate_feature_popularity_report

app = Flask(__name__)

@app.route('/api/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json.get('message')
    intents, entities = process_user_input(user_input)
    # Process intents and entities to generate a response
    response = f"Processed: {user_input}"  # Placeholder response
    return jsonify(response)

@app.route('/api/user', methods=['POST'])
def user_management():
    action = request.json.get('action')
    username = request.json.get('username')
    password = request.json.get('password')
    feature = request.json.get('feature')
    value = request.json.get('value')
    
    if action == 'create':
        create_user(username, password)
    elif action == 'update_preference':
        update_user_preference(username, feature, value)
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
