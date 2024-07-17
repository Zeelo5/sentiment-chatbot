from flask import Blueprint, request, jsonify
from transformers import pipeline
import nltk

# Initialize sentiment analysis model
nltk.download('vader_lexicon')
sentiment_analyzer = pipeline("sentiment-analysis")

suggest = Blueprint('suggest', __name__)

@suggest.route('/suggest', methods=['POST'])
# @suggest.route('/suggest', methods=['POST'])
def get_suggestions():
    user_input = request.json.get('text')
    print(f"User input: {user_input}")  # Debugging print
    sentiment_score = sentiment_analyzer(user_input)[0]['label']
    print(f"Sentiment score: {sentiment_score}")  # Debugging print

    if sentiment_score == 'NEGATIVE':
        response = {"message": "I'm sorry you're feeling down. Maybe check out some uplifting content!"}
    else:
        response = {"message": "Glad to hear you're doing well!"}
    
    return jsonify(response)

