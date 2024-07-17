from flask import Flask, render_template
from app.suggestions import suggest  # Import the Blueprint from suggestions.py

app = Flask(__name__)

# Register the Blueprint with a URL prefix (optional)
app.register_blueprint(suggest, url_prefix='/suggest')

@app.route('/')
def index():
    return render_template('index.html')
