from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from db import SQL, create_table
from datetime import datetime
import json

# Load in env varibles from .env file
load_dotenv()

db = SQL('chessGame.db')


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
    rows = db.execute('SELECT * FROM users WHERE username = ?', request.form.get('username'))

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]['password_hash'], request.form.get('password')):
        return apology('invalid username and/or password', 403)

    # Ensure email has been confirmed
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


@app.route('/games/list', methods=['GET', 'POST'])
def all_games():
    response_object = {'statusCode': 200}
    if request.method == 'POST':
        post_data = request.get_json()
        title = post_data['title']
        description = post_data['description']
        date = datetime.now().isoformat()
        source_text = post_data['sourceText']
        source_link = post_data['sourceLink']
        playing_white = post_data['playingWhite']
        playing_black = post_data['playingBlack']
        user_id = session['user_id']
        # Insert game listing into db
        game_listing = db.execute('''
            INSERT INTO games (
                title, 
                description, 
                date, 
                source_text, 
                source_link, 
                playing_white, 
                playing_black, 
                user_id, 
                revision_number
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ''', title, description, date, source_text, source_link, playing_white, playing_black, user_id, 0)
        # TODO: create game data db table
        create_table(db, "CREATE TABLE IF NOT EXISTS "+game_listing['id']+""" (
            id integer PRIMARY KEY,
            timestamp text DEFAULT CURRENT_TIMESTAMP,
            data text NOT NULL
        """)
        response_object = { 'statusCode': 200, 'game': { 'listing': game_listing } }
    else:
        response_object = { 'statusCode': 200, 'gamesList': db.execute('SELECT * FROM games').fetchall() }
    return jsonify(response_object)


@app.route('/games/<game_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def get_game_by_id(game_id):
    game_listing = db.execute('SELECT * FROM games WHERE id = ?', game_id)[0]
    if not game_listing: 
        return apology('Game not found', 404)
    elif request.method == 'POST':
        # Add game data
        post_data = request.get_json()
        game_data = db.execute('INSERT INTO '+game_listing['id']+' (data) VALUES(?)', json.dumps(post_data['gameData']))
        listing = db.execute('UPDATE games SET revision_number = ? WHERE id = ?', game_data['id'], game_listing['id'])
        response_object = { 'statusCode': 200, 'game': { 'listing': listing, 'data': game_data } }
    elif request.method == 'GET':
        # Send game data
        game_data = db.execute('SELECT * FROM '+game_listing['id']+' WHERE id = ?', game_listing['revision_number'])
        response_object = { 'statusCode': 200, 'gameData': game_data }
    elif request.method == 'PUT': 
        # Merge any new values into game_listing
        post_data = request.get_json()
        updated_data = { **game_listing, **post_data }

        # Update game info
        listing = db.execute('''
            UPDATE games SET (
                title, 
                description, 
                source_text, 
                source_link, 
                playing_white, 
                playing_black,
                revision_number
            ) VALUES(?, ?, ?, ?, ?, ?) WHERE id = ?
        ''', updated_data['title'], updated_data['description'], updated_data['source_text'], updated_data['source_link'], updated_data['playing_white'], updated_data['playing_black'], updated_data['revision_number'], game_listing['id'])
    elif request.method == 'DELETE':
        response_object = {'statusCode': 501}
        # TODO: Remove game listing (and queue deletion?)
    return jsonify(response_object)


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