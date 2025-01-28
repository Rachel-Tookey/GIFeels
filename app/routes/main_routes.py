from app.data.repository import *
from app.web_client.external_api_clients import QuoteAPI, JokeAPI, MoodDict
from flask import render_template, request, redirect, session, Blueprint, jsonify
from datetime import datetime
from app.utils.flask_helpers import flash_error, flash_notification
from app.wrappers.login_wrapper import login_required
from app.utils.dict_utils import clean_dict
from app.settings.oauth_providers import googleOauth
from app.utils.date_utils import get_utc_date

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def mood_checkin():
    if 'mood_dict' not in session:
        emotions_api = MoodDict()
        emotions_dict = emotions_api.make_dict()
        session['mood_dict'] = emotions_dict
    return render_template("mood.html", emotions=clean_dict(session['mood_dict']))


@main.route('/choice/<emotion_id>', methods=['GET', 'POST'])
def choice(emotion_id):
    session['emotion'] = emotion_id
    session['mood_url'] = session['mood_dict'][emotion_id]
    session['mood_url_gif'] = session['mood_dict'][f"{emotion_id}_gif"]
    return render_template("choice.html", emotion=emotion_id)


@main.route('/save_choice', methods=['GET'])
@login_required
def save_choice():
    choice = session['choice']
    entry_saved_already = check_entry_exists(session['user_id'], session['date'])
    if entry_saved_already:
        flash_notification("You have already saved an entry for today")
    else:
        today_emotion(session['user_id'], session['emotion'], session['mood_url'], session['mood_url_gif'], session['date'], session['choice'], session[choice])
        if check_entry_exists(session['user_id'], session['date']):
            flash_notification("Your entry has been saved.")
            return redirect('/journal')
        else:
            flash_error("Something went wrong. Please try again later")
            return redirect(request.referrer)
    return redirect(f'/{choice}')


@main.route('/quote', methods=['GET', 'POST'])
def quote_of_the_day():
    if 'quote' not in session:
        quote_api = QuoteAPI()
        result = quote_api.unpack()
        session['quote'] = result[0]
        session['author'] = result[1]
    if request.method == "POST":
        session['choice'] = "quote"
        return redirect('/save_choice')
    return render_template("quote.html", quote=session['quote'], author=session['author'])


@main.route('/joke', methods=['GET', 'POST'])
def joke_generator():
    if 'joke' not in session:
        joke_api = JokeAPI()
        result = joke_api.unpack()
        session['joke'] = result
    if request.method == "POST":
        session['choice'] = "joke"
        return redirect('/save_choice')
    return render_template("joke.html", joke=session['joke'])


@main.route('/journal', methods=['GET', 'POST'])
@login_required
def add_journal_entry():
    if request.method == 'POST':
        content = request.form.get('textarea')
        if not content:
            flash_error('Journal is empty')
        elif len(content) > 350:
            flash_error("Oops! Journal entries must be 350 characters or less...")
        elif not check_entry_exists(session['user_id'], session['date']):
            flash_notification("You need to save today's emotion first!")
        elif check_journal_entry_exists(session['user_id'], session['date']):
            flash_notification('You have already submitted a diary entry for this date')
        else:
            add_journal(content, session['user_id'], session['date'])
            if check_journal_entry_exists(session['user_id'], session['date']):
                flash_notification("Your entry has been saved.")
                return redirect('/overview')
            else:
                flash_error('Something went wrong. Please try again later.')
    return render_template("journal.html")


@main.route('/overview', methods=['GET', 'POST'])
@login_required
def show_overview():
    if request.method == "POST":
        session.pop('_flashes', None)
        user_month = request.form.get('month')[0:15]
        if user_month:
            date_object = datetime.strptime(user_month, "%a %b %d %Y")
            emotion_list = get_month_emotions(session['user_id'], int(date_object.month), int(date_object.year))
            date_list = get_entry_dates_month(session['user_id'], int(date_object.month), int(date_object.year))
            return jsonify({'output': emotion_list, 'dates': date_list})
    return render_template("overview.html")


@main.route('/archive/<date>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def show_archive_by_date(date):
    user_entry = get_records(session['user_id'], date)
    user_reflections = get_reflections(user_entry.id)
    if user_entry is None:
        flash_notification(f"No records saved on {date}")
        return redirect('/overview')
    record = {'emotion': user_entry.emotion, 'gif_url': user_entry.giphy_url, 'choice': user_entry.choice, 'quote_joke': user_entry.content,
              'diary': f"Click to add a diary entry for {date}!" if user_entry.diary_entry is None else user_entry.diary_entry}
    if request.method == 'POST':
        print(request.form.get('content'))
        save_reflection(user_entry.id, get_utc_date(), request.form.get('content'))
    if request.method == 'PUT':
        add_journal(request.form.get('content'), session['user_id'], date)
    if request.method == 'DELETE':
        delete_entry(user_id=session['user_id'], date=date)
    return render_template("archive.html", date=date, record=record, reflections=user_reflections)

