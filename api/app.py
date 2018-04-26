from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Home"


@app.route('/get_title', methods=['GET', 'POST'])
def playlist_title_get():
    if request.method == 'GET':
        return "Use POST"

    body = request.json

    # do something with it

    return jsonify({
        'name': 'BBB'
    })

