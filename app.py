from db_utils import get_user_id, today_emotion, add_new_user, check_email, check_username, check_entry_journal, verify_cred, check_entry, add_journal
from flask import Flask, render_template, request, flash, redirect, session
from config import SECRET_KEY
from helper_oop import QuoteAPI, JokeAPI, MoodDict
from registration_form import RegistrationForm
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


# Choose how you feel
@app.route('/', methods=['GET', 'POST'])
def mood_checkin():
    emotions_api = MoodDict()
    emotions_dict = emotions_api.make_dict()
    session['mood_dict'] = emotions_dict # in case we do want to save the giphy url - delete if not
    return render_template("mood.html", emotions=emotions_dict)


# Accessed after choosing a feeling - allows user to choose between getting a joke or a quote
@app.route('/choice/<id>', methods=['GET', 'POST'])
def choice(id):
    session['emotion'] = id
    session['mood_url'] = session['mood_dict'][id] # in case we do want to save the giphy url - delete if not
    return render_template("choice.html", emotion=id)


# Get the quote of the day
@app.route('/quote', methods=['GET', 'POST'])
def quote_of_the_day():
    quote_api = QuoteAPI()
    result = quote_api.unpack()
    quote = result[0]
    author = result[1]
    if request.method == "POST":
        if 'user' not in session:
            return redirect('/login')
        else:
            response = check_entry(session['user_id'], session['date'])
            if response == True:
                flash("You have already saved an entry for today", "notification")
            elif response == False:
                today_emotion(session['user_id'], session['emotion'], session['mood_url'], session['date'], 'Quote', quote)
                response_two = check_entry(session['user_id'], session['date'])
                if response_two:
                    return redirect('/journal')
            else:
                flash("Something went wrong. Please try again later", "error")
    return render_template("quote.html", quote=quote, author=author)


# Get a joke
@app.route('/joke', methods=['GET', 'POST'])
def joke_generator():
    joke_api = JokeAPI()
    result = joke_api.unpack()
    if request.method == "POST":
        if 'user' not in session:
            return redirect('/login')
        else:
            response = check_entry(session['user_id'], session['date'])
            if response == True:
                flash("You have already saved an entry for today", "notification")
            elif response == False:
                today_emotion(session['user_id'], session['emotion'], session['mood_url'], session['date'], 'Joke', result)
                response_two = check_entry(session['user_id'], session['date'])
                if response_two:
                    return redirect('/journal')
            else:
                flash("Something went wrong. Please try again later", "error")
    return render_template("joke.html", joke=result)


# Save a journal entry
@app.route('/journal', methods=['GET', 'POST'])
def add_journal_entry():
    session.pop('_flashes', None)
    if request.method == 'POST':
        content = request.form.get('textarea')
        if 'user' not in session:
            return redirect('/login')
        elif not content:
            flash('Journal is empty', "notification-error")
        else:
            response = check_entry_journal(session['user_id'], session['date'])
            if response == True:
                flash('You have already submitted a diary entry for this date', "notification")
            elif response == False:
                add_journal(content, session['user_id'], session['date'])
                response_two = check_entry_journal(session['user_id'], session['date'])
                if response_two:
                    return redirect('/overview')
            else:
                flash('Something went wrong. Please try again later.', "error")
    return render_template("journal.html")


# Get calendar view of your entries + stats of moods
@app.route('/overview', methods=['GET'])
def show_overview():
    if 'user' not in session:
        return redirect('/login')
    return render_template("overview.html")


# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        content = {}
        for item in ["FirstName", "LastName", "Username", "email", "password", "confirm", "accept_tos"]:
            content[item] = request.form.get(item)

        if content['password'] != content['confirm']:
            flash('Password and Password Confirmation do not match', "error")
        else:
            content['password'] = bcrypt.hashpw(content['password'].encode('utf-8'), bcrypt.gensalt())
            content['password'] = content['password'].decode()
            content['confirm'] = content['password']

        if check_email(content['email']):
            flash('Email already registered')
        elif check_username(content['Username']):
            flash('Username already in use', "error")
        else:
            add_new_user(content)
            if check_email(content['email']):
                return redirect('/login/new')
            else:
                flash('We were unable to register you at this time. Please try again later', "error")
    return render_template("register.html", form=form)


# Log in with credentials
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<user>', methods=['GET', 'POST'])
def user_login(user=""):
    session.pop('_flashes', None)
    if user == "new":
        flash("Your account has been created. Please login.", "notification")
    elif user == "out":
        session.clear()
        flash("You have been logged out. See you soon!", "notification")
    if request.method == 'POST':
        session.clear()
        username = request.form.get('uname')
        password = request.form.get('password')
        if not check_username(username):
            flash("This username does not exist", "error")
        else:
            response = verify_cred(username, password)
            if not response:
                flash("Username and Password do not match", "error")
            elif response:
                session['user'] = username
                session['user_id'] = get_user_id(username)
                session['date'] = datetime.today().strftime('%Y-%m-%d')
                return redirect('/')
            else:
                flash("Something went wrong! Please try again later", "error")
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, port=5500)