import pandas as pd
from transformers import pipeline
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('vader_lexicon')



faq_df = pd.read_csv(r"D:\\New folder\Documents\sentiment-chatbot\\Mental_Health_FAQ.csv")

sentiment_analyzer = pipeline("sentiment-analysis")
empathetic_responses = {
    "sad": [
        "I'm sorry you're feeling this way. Remember, it's okay to feel down sometimes.",
        "It sounds like you're having a tough time. I'm here for you!",
        "Things may seem difficult now, but they can get better.",
        "I'm here to listen. Do you want to talk more about what's making you sad?"
    ],
    "happy": [
        "That's wonderful to hear! Keep up the positive vibes!",
        "I'm glad you're feeling good! Is there anything else I can help with?",
        "Great to hear you're in a good mood! How can I assist you today?",
        "Your positive energy is great! How can I make your day even better?"
    ],
    "default": [
        "I'm here to help with any questions or concerns you might have.",
        "Let me know if there's anything specific you'd like to discuss.",
        "Thanks for sharing that with me.",
        "Okay, if you need anything, just let me know."
    ]
}

# Song recommendations based on mood
song_recommendations = {
    "sad": [
        "Someone Like You by Adele",
        "Fix You by Coldplay",
        "Hurt by Johnny Cash",
        "The Night We Met by Lord Huron"
    ],
    "happy": [
        "Happy by Pharrell Williams",
        "Can't Stop the Feeling! by Justin Timberlake",
        "Uptown Funk by Mark Ronson ft. Bruno Mars",
        "Shake It Off by Taylor Swift"
    ],
    "relaxed": [
        "Weightless by Marconi Union",
        "Sunset Lover by Petit Biscuit",
        "River Flows in You by Yiruma",
        "Budapest by George Ezra"
    ],
    "energetic": [
        "Eye of the Tiger by Survivor",
        "Don't Stop Believin' by Journey",
        "Stronger by Kanye West",
        "Can't Hold Us by Macklemore & Ryan Lewis"
    ]
}

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
        text_lower = text.lower()
        
        if any(keyword in text_lower for keyword in ["sad", "unhappy", "depressed", "down"]):
            response = random.choice(empathetic_responses["sad"])
            response += "\n\nHere are some songs that might help lift your spirits:\n" + "\n".join(song_recommendations["sad"])
        elif any(keyword in text_lower for keyword in ["happy", "joyful", "excited", "good"]):
            response = random.choice(empathetic_responses["happy"])
            response += "\n\nGlad you're feeling good! How about some more upbeat tunes:\n" + "\n".join(song_recommendations["happy"])
        elif any(keyword in text_lower for keyword in ["relaxed", "calm", "chilled"]):
            response = random.choice(empathetic_responses["default"])
            response += "\n\nHere are some relaxing songs you might enjoy:\n" + "\n".join(song_recommendations["relaxed"])
        elif any(keyword in text_lower for keyword in ["energetic", "motivated", "pumped"]):
            response = random.choice(empathetic_responses["default"])
            response += "\n\nNeed an energy boost? Check out these songs:\n" + "\n".join(song_recommendations["energetic"])
        else:
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
