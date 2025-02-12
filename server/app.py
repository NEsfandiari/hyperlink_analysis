from flask import Flask, make_response
from flask_cors import CORS
from links import top_100
import json

app = Flask(__name__)
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return make_response("Elderblog Analysis Server :)")


@app.route('/data/links/<params>')
def return_top(params):
    params = params.split('-')

    start_date = int(params[0])
    end_date = int(params[1])
    non_ribbonfarm = True if params[2] == 'true' else False
    search = None if params[3] == 'false' else params[3]

    data = top_100(start_date, end_date, non_ribbonfarm, search)
    return json.dumps(data)


@app.route('/data/words')
def return_words():
    with open('./data/word_choice_data.txt', 'r') as f:
        data = json.load(f)
        if len(data) > 0:
            return json.dumps(data)


@app.route('/data/posts')
def return_posts():
    with open('./data/eigen_post_data.txt', 'r') as f:
        data = json.load(f)
        if len(data) > 0:
            return json.dumps(data)


if __name__ == '__main__':
    print('Starting Flask!')
    app.run(debug=True)
