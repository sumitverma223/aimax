# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy data for recommendations
recommendations = {
    'user1': [
        {'title': 'The Future of AI', 'body': 'Exploring the next advancements in artificial intelligence.'},
        {'title': 'Top Machine Learning Techniques', 'body': 'A guide to the most effective machine learning techniques.'}
    ],
    'user2': [
        {'title': 'Healthy Eating Tips', 'body': 'Advice for a balanced and healthy diet.'},
        {'title': 'Fitness Routines', 'body': 'Effective exercise routines for different fitness levels.'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    user_recommendations = recommendations.get(user_id, [])
    return jsonify(user_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
