from transformers import pipeline
import nltk
import tensorflow as tf
import tf_keras  # This line checks if `tf-keras` is properly installed

# Test sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
print("Packages imported successfully and sentiment analysis pipeline is working.")
