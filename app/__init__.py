

from flask import Flask
import pandas as pd

def create_app():
    app = Flask(__name__)
    
    # Load the FAQ CSV file
    faq_df = pd.read_csv(r"D:\\New folder\Documents\sentiment-chatbot\\Mental_Health_FAQ.csv")

    with app.app_context():
        from .routes import suggest_bp
        app.register_blueprint(suggest_bp)
        app.faq_df = faq_df  # Make the DataFrame available globally within the app

    return app
