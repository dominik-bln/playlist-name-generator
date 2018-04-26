from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return "Home"


@app.route('/get_title', methods=['GET', 'POST'])
def playlist_title_get():
    if request.method == 'GET':
        return "Use POST"

    body = request.json
    # do something with it
    print(body)

    return jsonify({
      'playlist_name': 'test title'
    })
