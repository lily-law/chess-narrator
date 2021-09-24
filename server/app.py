from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from db import SQL

# Load in env varibles from .env file
load_dotenv()

db = SQL('chessGame.db')

# Temporary data store until database is added
# DB = {
#     'users': [
#         {
#             'id': '0',
#             'person_id': '2',
#             'email_hash': 'abc',
#             'password_hash': 'abc',
#             'username': 'abc',
#             'email_confirmed': '2021-07-26T11:37:24.688Z'
#         }
#     ],
#     'people': [
#         {
#             'id': '0',
#             'name': 'default user 1',
#         },
#         {
#             'id': '1',
#             'name': 'default user 2',
#         },
#         {
#             'id': '2',
#             'name': 'Some User',
#             'avatar': '',
#             'user_id': '0'
#         }
#     ],
#     'games': [
#         {
#             'id': '0',
#             'title': 'Someone vs Someone Else',
#             'description': 'An example game to use as dummy data',
#             'date': '2021-07-26T11:37:24.688Z',
#             'source': {
#                 'text': 'Made up by me',
#                 'link': 'http://example.com'
#             },
#             'playingWhite': '0',
#             'playingBlack': '1',
#             'user_id': '0'
#         }
#     ]
# }

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# TODO: limit origins for production
CORS(app, resources={r'/*': {'origins': '*'}})

#####
# User auth logic
# based from CS50's finance pset9
####

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/login', methods=['POST'])
def login():
    '''Log user in'''

    # Forget any user_id
    session.clear()

    # Ensure username was submitted
    if not request.form.get('username'):
        return apology('must provide username', 403)

    # Ensure password was submitted
    elif not request.form.get('password'):
        return apology('must provide password', 403)

    # Query database for username
    # TODO: swap once DB is setup
    rows = filter(lambda user: (user['username'] == request.form.get('username')), db['users'])
    ## rows = db.execute('SELECT * FROM users WHERE username = ?', request.form.get('username'))

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]['password_hash'], request.form.get('password')):
        return apology('invalid username and/or password', 403)

    if not rows[0]['email_confirmed']:
        return apology('follow link in email confirmation', 400)

    # Remember which user has logged in
    session['user_id'] = rows[0]['id']

    # Return user data to client
    return jsonify(rows[0])


@app.route('/logout')
def logout():
    '''Log user out'''

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return True


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''Register user'''

    username = request.form.get('username')
    # Ensure username was submitted
    if not username:
        return apology('must provide username', 400)

    # Check if username already exists
    if len(db.execute('SELECT * FROM users WHERE username = ?', username)) > 0:
        return apology('username already taken', 400)

    password = request.form.get('password')
    # Ensure password was submitted
    if not password:
        return apology('must provide password', 400)

    # Ensure password matches confirmation
    if password != request.form.get('confirmation'):
        return apology('passwords must match', 400)

    # Add new user to DB and store their id in current session
    session['user_id'] = db.execute('INSERT INTO users (username, hash) VALUES(?, ?)', username, generate_password_hash(password))

    # Redirect user to home page and flash welcome message
    flash(f'Welcome {username}, thanks for joining!')
    return redirect('/')

@app.route('/register/confirmation', methods=['POST'])
def send_email_confirmation():
    '''Resend email confirmation'''
    # TODO
    print('Resend email confirmation')

@app.route('/register/confirmation/<token>', methods=['GET'])
def confirm_email():
    '''Confirm email'''
    # TODO
    print('enable account')

@app.route('/login/password/<token>', methods=['GET'])
def reset_password():
    '''Reset password'''
    # TODO
    print(f'reset password, token: {escape(token)}')


@app.route('/login/reset', methods=['POST'])
def email_reset_token():
    '''Send password reset link'''
    # TODO
    print('send email reset')


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'statusCode': 200}
    if request.method == 'POST':
        post_data = request.get_json()
        db.execute('INSERT INTO games (title) VALUES(?)', post_data.get('title'))
        response_object['message'] = 'Game added!'
    else: 
        response_object['games'] = db.execute('SELECT * FROM games').fetchall()
    return jsonify(response_object)


@app.route('/game/<game_id>', methods=['GET'])
def get_game_by_id():
    response_object = {'statusCode': 200}
    # TODO: Update game


@app.route('/game/<uuid:game_id>', methods=['PUT'])
def update_game_by_id():
    response_object = {'statusCode': 200}
    # TODO: Update game


# if __name__ == '__main__':
#     app.run()

#####
# Error handling
# based from CS50's finance pset9
####

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return { 'statusCode': code, 'message': escape(message) }


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)