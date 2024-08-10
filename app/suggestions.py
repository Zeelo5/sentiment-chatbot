import pandas as pd
from transformers import pipeline
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('vader_lexicon')



faq_df = pd.read_csv(r"D:\\New folder\Documents\sentiment-chatbot\\Mental_Health_FAQ.csv")

sentiment_analyzer = pipeline("sentiment-analysis")
def suggest(text):
    # Check for FAQ match
    questions = faq_df['Question'].tolist()
    tfidf_vectorizer = TfidfVectorizer().fit_transform(questions)
    user_tfidf = TfidfVectorizer().fit(questions).transform([text])
    similarity = cosine_similarity(user_tfidf, tfidf_vectorizer).flatten()
    max_similarity_idx = similarity.argmax()

    if similarity[max_similarity_idx] > 0.7:
        response = faq_df.iloc[max_similarity_idx]['Answer']
    else:
        # Sentiment analysis
        sentiment_score = sentiment_analyzer(text)[0]
        sentiment_label = sentiment_score['label']
        sentiment_confidence = sentiment_score['score']

        response_database = {
            "negative_responses": [
                "I'm sorry you're feeling down. Maybe check out some uplifting content!",
                "It sounds tough. Hang in there!",
                "Don't worry, things will get better!",
                "Sorry to hear that. Want to talk about it?"
            ],
            "positive_responses": [
                "Glad to hear you're doing well!",
                "That's great to hear!",
                "Wonderful news!",
                "Keep up the positive vibes!"
            ],
            "neutral_responses": [
                "I'm here to help with sentiment analysis.",
                "Let me know if there's anything specific you'd like to discuss.",
                "Thanks for sharing that.",
                "Okay, noted."
            ]
        }

        if sentiment_label == 'NEGATIVE':
            response = random.choice(response_database['negative_responses'])
        elif sentiment_label == 'POSITIVE':
            response = random.choice(response_database['positive_responses'])
        else:
            response = random.choice(response_database['neutral_responses'])

        response += f" (Confidence: {sentiment_confidence:.2f})"

    return response


if __name__ == "__main__":
    user_input = input("You: ")
    bot_response = suggest(user_input)
    print(f"Bot: {bot_response}")
