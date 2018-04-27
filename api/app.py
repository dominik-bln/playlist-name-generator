from flask import Flask, request, jsonify
from flask_cors import CORS
from title_generator import TitleGenerator

app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return "Home"


tg = None


@app.before_first_request
def init_title_generator():
    global tg
    config = {
        'playlist_titles_file': '/data/playlist_titles_full.csv',
        'playlist_data_file': '/data/playlist_train_meta.csv',
        'centroids_mat_file': '/data/kmeans_mat'}

    google_model_path = '/data/GoogleNews-vectors-negative300.bin.gz'

    tg = TitleGenerator(config)
    tg.load_word2vec_model(google_model_path)
    print('Loading data...')
    tg.load_data()


@app.route('/get_title', methods=['GET', 'POST'])
def playlist_title_get():
    global tg
    if request.method == 'GET':
        return "Use POST"

    # tg.model = model
    # Get data from UI
    ui_data = request.get_json()
    # do something with it
    print(ui_data)
    print('Running...')
    title = tg.generate_title(ui_data['tracks'])

    return jsonify({
        'playlist_name': title
    })
