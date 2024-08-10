from flask import Blueprint, request, jsonify, render_template
from app.suggestions import suggest  # Import the function, not the Blueprint

suggest_bp = Blueprint('suggest', __name__)

@suggest_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # This renders the index.html template

@suggest_bp.route('/suggest', methods=['POST'])
def suggest_route():
    data = request.get_json()
    text = data.get('text', '')
    response = suggest(text)  # Call the suggest function
    return jsonify(response)
