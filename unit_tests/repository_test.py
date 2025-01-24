from app.data import repository
import unittest
from app import db, create_app
from app.models.user import User
from app.models.localuser import LocalUser
from app.models.entries import Entries
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text


class TestWebApp(unittest.TestCase):

    def setUp(self):
        config_override = {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'SECRET_KEY': 'test_key'
        }

        self.app = create_app(test_config=config_override)
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        db.create_all()
        self.populate_db()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def populate_db(self):
        test_user_one = User(id=1, username="test_user", email="test@email")
        test_user_two = User(id=2, username="another_user", email="test2@email")

        db.session.add(test_user_one)
        db.session.add(test_user_two)

        test_localuser_one = LocalUser(id=1, user_id=1, first_name="test", family_name="user", password="123", accept_tos=True)
        test_localuser_two = LocalUser(id=2, user_id=2, first_name="another", family_name="user", password="abc", accept_tos=True)

        db.session.add(test_localuser_one)
        db.session.add(test_localuser_two)

        date = datetime(2024, 5, 31).date()
        test_entries_one = Entries(id=1, user_id=1, entry_date=date, emotion='frustrated', giphy_url='https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', choice='Joke', content='What did the pirate say on his 80th birthday? Aye Matey!')

        date = datetime(2025, 5, 31).date()
        test_entries_two = Entries(id=2, user_id=2, entry_date=date, emotion='happy', giphy_url='https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', choice='Joke', content='What did the pirate say on his 80th birthday? Aye Matey!', diary_entry='Super frustrated!')

        date = datetime(2026, 5, 31).date()
        test_entries_three = Entries(id=3, user_id=1, entry_date=date, emotion='angry', giphy_url='https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', choice='Quote', content='What did the pirate say on his 80th birthday? Aye Matey!', diary_entry='Super frustrated!')


        db.session.add(test_entries_one)
        db.session.add(test_entries_two)
        db.session.add(test_entries_three)


        db.session.commit()

    def test_username_exists(self):
        resp = repository.check_username_exists("test_user")
        assert resp is True

    def test_username_does_not_exist(self):
        resp = repository.check_username_exists("wrong_user")
        assert resp is False

    def test_get_id_by_username(self):
        resp = repository.get_user_id_by_username("another_user")
        assert resp == 2

    def test_get_userid_by_email(self):
        resp = repository.get_user_id_by_email("test@email")
        assert resp == 1

    def test_get_password_by_id(self):
        resp = repository.get_password(2)
        assert resp == 'abc'

    def test_email_exists(self):
        resp = repository.check_email_exists("test@email")
        assert resp is True

    def test_email_does_not_exist(self):
        resp = repository.check_email_exists("wrong@email")
        assert resp is False

    def test_check_entry_exists(self):
        date = datetime(2024, 5, 31).date()
        resp = repository.check_entry_exists(1, date)
        assert resp is True

    def test_check_entry_does_not_exist(self):
        date = datetime(2024, 5, 30)
        resp = repository.check_entry_exists(1, date)
        assert resp is False

    def test_returns_correct_entry(self):
        date = datetime(2024, 5, 31).date()
        test_entries_one = Entries(id=1, user_id=1, entry_date=date, emotion='frustrated', giphy_url='https://media4.giphy.com/media/xUNd9AWlNxNgnxiIxO/200w.mp4?cid=0303f60aw8n6rbf1tb5l49kgndy9ynu24ksk32rvhu477sdi&ep=v1_gifs_search&rid=200w.mp4&ct=g', choice='Joke', content='What did the pirate say on his 80th birthday? Aye Matey!', diary_entry='Super frustrated!')
        resp = repository.get_records(1, date)
        assert resp.giphy_url == test_entries_one.giphy_url
        assert resp.emotion == test_entries_one.emotion
        assert resp.choice == test_entries_one.choice

    def test_returns_null_entry(self):
        date = datetime(2024, 5, 31).date()
        resp = repository.get_records(2, date)
        assert resp is None

    def test_delete_entry(self):
        date = datetime(2025, 5, 31).date()
        resp = repository.get_records(2, date)
        assert resp is not None
        repository.delete_entry(2, date)
        resp = repository.get_records(2, date)
        assert resp is None

    def test_check_journal_entry_exists(self):
        date = datetime(2026, 5, 31).date()
        resp = repository.check_journal_entry_exists(1, date)
        assert resp is True

    def test_check_journal_entry_null(self):
        date = datetime(2024, 5, 31).date()
        resp = repository.check_journal_entry_exists(1, date)
        assert resp is False

    def test_get_emotion_count_one(self):
        resp = repository.get_emotion_count(1, 'frustrated', 5, 2024)
        assert resp is 1

    def test_get_emotion_count_zero(self):
        resp = repository.get_emotion_count(1, 'frustrated', 4, 2024)
        assert resp is 0

    def test_get_month_emotions(self):
        expected_list =[{'name': 'happy', 'value': 0},
 {'name': 'calm', 'value': 0},
 {'name': 'sad', 'value': 0},
 {'name': 'worried', 'value': 0},
 {'name': 'frustrated', 'value': 1},
 {'name': 'angry', 'value': 0}]

        resp = repository.get_month_emotions(1, 5, 2024)
        assert expected_list == resp

    def test_get_month_emotions_none(self):
        expected_list = [{'name': 'happy', 'value': 0},
                         {'name': 'calm', 'value': 0},
                         {'name': 'sad', 'value': 0},
                         {'name': 'worried', 'value': 0},
                         {'name': 'frustrated', 'value': 0},
                         {'name': 'angry', 'value': 0}]
        resp = repository.get_month_emotions(1, 1, 2024)
        assert expected_list == resp

    def test_emotions_added(self):
        date = datetime(2027, 5, 31).date()
        resp = repository.check_entry_exists(1, date)
        assert resp is False
        repository.today_emotion(user_id=1, date=date, emotion='angry', giphy_url='www.giphy_url', choice='Joke', response='jks')
        resp = repository.check_entry_exists(1, date)
        assert resp is True

    def test_journal_added(self):
        date = datetime(2027, 5, 31).date()
        repository.today_emotion(user_id=1, date=date, emotion='angry', giphy_url='www.giphy_url', choice='Joke', response='jks')
        resp = repository.check_journal_entry_exists(1, date)
        assert resp is False
        repository.add_journal("New journal", 1, date)
        resp = repository.check_journal_entry_exists(1, date)
        assert resp is True


    def test_add_local_user_fk_fail(self):
        db.session.execute(text("PRAGMA foreign_keys = ON"))
        localuser = { 'firstname' : "new", 'lastname' : "user", 'password' : "abcdefg" }
        with self.assertRaises(IntegrityError):
            repository.add_new_local_user(20, user=localuser)


if __name__ == "__main__":
    unittest.main()