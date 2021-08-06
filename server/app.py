from flask import Flask, jsonify, request
from flask_cors import CORS

# Temporary data store until database is added
DB = {
    'users': [
        {
            'id': '0',
            'person_id': '2',
            'email_hash': 'abc',
            'password_hash': 'abc'
        }
    ],
    'people': [
        {
            'id': '0',
            'name': 'default user 1',
        },
        {
            'id': '1',
            'name': 'default user 2',
        },
        {
            'id': '2',
            'name': 'Some User',
            'avatar': '',
            'user_id': '0'
        }
    ],
    'games': [
        {
            'id': '0',
            'title': 'Someone vs Someone Else',
            'description': 'An example game to use as dummy data',
            'date': '2021-07-26T11:37:24.688Z',
            'source': {
                'text': 'Made up by me',
                'link': 'http://example.com'
            },
            'playingWhite': '0',
            'playingBlack': '1',
            'user_id': '0'
        }
    ]
}

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        DB['games'].append({
            'title': post_data.get('title'),
            # TODO: add remaining fields
        })
        response_object['message'] = 'Game added!'
    else: 
        response_object['games'] = DB['games']
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()