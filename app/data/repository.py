from app import db
from app.models.entries import Entries
from app.models.user import User
from app.models.localuser import LocalUser
from app.models.authuser import AuthUser
from app.models.reflections import Reflections
from sqlalchemy import and_, extract


def today_emotion(user_id, emotion, giphy_url, giphy_url_gif, date, choice, response):
    new_entry = Entries(user_id=user_id, entry_date=date, emotion=emotion, giphy_url=giphy_url, giphy_url_gif=giphy_url_gif, choice=choice.capitalize(), content=response)
    db.session.add(new_entry)
    db.session.commit()


def add_journal(journal_entry, user_id, date):
    entry = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.entry_date == date)
    ).first()
    entry.diary_entry = journal_entry
    db.session.commit()


def get_user_id_by_username(username):
    return User.query.filter_by(username=username).first().id


def get_user_id_by_email(email):
    return User.query.filter_by(email=email).first().id


def get_password(user_id):
    return LocalUser.query.filter_by(user_id=user_id).first().password


def add_new_global_user(email, username=None):
    new_user = User(email=email, username=username)
    db.session.add(new_user)
    db.session.commit()


def add_new_local_user(user_id, user):
    new_user = LocalUser(user_id=user_id, first_name=user['firstname'], family_name=user['lastname'], password=user['password'], accept_tos=True)
    db.session.add(new_user)
    db.session.commit()


def add_new_auth_user(user_id, user):
    new_user = AuthUser(user_id=user_id, auth0_id=user['sub'], name=user['name'], accept_tos=True)
    db.session.add(new_user)
    db.session.commit()


def check_email_exists(email):
    user = User.query.filter_by(email=email).first()
    return user is not None


def check_username_exists(username):
    user = User.query.filter_by(username=username).first()
    return user is not None


def check_entry_exists(user_id, date):
    entry = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.entry_date == date)
    ).first()
    return entry is not None


def get_records(user_id, date):
    entry = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.entry_date == date)
    ).first()
    return entry


def delete_entry(user_id, date):
    entry = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.entry_date == date)
    ).first()
    if entry:
        db.session.delete(entry)
        db.session.commit()


def check_journal_entry_exists(user_id, date):
    entry = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.entry_date == date)
    ).first()
    if entry is not None and entry.diary_entry is not None:
        return True
    return False


def get_emotion_count(user_id, emotion, month, year):
    emotion_count = Entries.query.filter(
        and_(Entries.user_id == user_id, Entries.emotion == emotion,
             extract('month', Entries.entry_date) == month,
             extract('year', Entries.entry_date) == year,
             )).count()
    return emotion_count


def get_month_emotions(user_id, month, year):
    emotion_dict = []
    emotion_list = ["happy", "calm", "sad", "worried", "frustrated", "angry"]
    for emotion in emotion_list:
        emotion_count = {}
        count = get_emotion_count(user_id, emotion, month, year)
        emotion_count['name'] = emotion
        emotion_count['value'] = count
        emotion_dict.append(emotion_count)
    return emotion_dict


def get_entry_dates_month(user_id, month, year):
    colors = {
        "happy": "#FFEEA8",
        "calm": "#D5E386",
        "sad": "#D9E8F5",
        "worried": "#D9D9D9",
        "frustrated": "#F2BDC7",
        "angry": "#ff9c78"}
    date_list = {}
    entries = Entries.query.filter(
        and_(Entries.user_id == user_id,
             extract('month', Entries.entry_date) == month,
             extract('year', Entries.entry_date) == year,
             ))
    for entry in entries:
        date_list[entry.entry_date.strftime("%Y%m%d")] = {'color': colors[entry.emotion], 'url': entry.giphy_url_gif}
    return date_list


def get_reflections(entry_id):
    reflections = Reflections.query.filter(Reflections.entry_id == entry_id)
    return reflections


def save_reflection(entry_id, date, content):
    new_reflection = Reflections(entry_id=entry_id, reflection_date=date, content=content)
    db.session.add(new_reflection)
    db.session.commit()