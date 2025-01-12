import unittest
from flask_testing import TestCase
from app import create_app, db

class MyTest(TestCase):

    def create_app(self):
        config_override = {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'WTF_CSRF_ENABLED': False,
            'SECRET_KEY' : 'test_key'
        }
        app = create_app(test_config=config_override)
        return app

    def test_template_rendered(self):
        self.client.get('/')
        self.assert_template_used('mood.html')

    def test_template_rendered_quote(self):
        self.client.get('/quote')
        self.assert_template_used('quote.html')

    def test_template_rendered_choice(self):
        with self.client:
            with self.client.session_transaction() as test_sess:
                test_sess['mood_dict'] = {'sad': ''}
            self.client.get('/choice/sad')
            self.assert_template_used('choice.html')

    def test_template_rendered_joke(self):
        self.client.get('/joke')
        self.assert_template_used('joke.html')

    def test_template_rendered_journal(self):
        with self.client.session_transaction() as test_sess:
            test_sess['user'] = 'testuser'
        self.client.get('/journal')
        self.assert_template_used('journal.html')

    def test_overview_redirect(self):
        response = self.client.get('/overview', follow_redirects=False)
        self.assert_status(response, 302)

    def test_form_submission_wrongpw(self):
        self.client.post('/register', data={'FirstName': 'Rachel', 'LastName': 'Tookey', "Username": "Rachel1993", "email": "rachel@tookey.com", "password":"snow", "confirm":"rain", "accept_tos":True})
        self.assert_message_flashed('Password and Password Confirmation do not match', "error")

    def test_form(self):
        response = self.client.post('/register', data={'FirstName': 'Rachel', 'LastName': 'Tookey', "Username": "Rachel1993", "email": "rachel@tookey.com", "password":"snow", "confirm":"snow", "accept_tos":True}, follow_redirects=True)
        self.assert_200(response)

    def test_404(self):
        response = self.client.get('/hello')
        self.assert404(response)

    def test_login_200(self):
        response = self.client.get('/login')
        self.assert_200(response, 200)

    def test_login_credentials_200(self):
        response = self.client.post('/login', data={'uname': 'JoDoe', 'password': 'password123'}, follow_redirects=True)
        self.assert_200(response, 200)

    def test_session(self):
        with self.client.session_transaction() as test_sess:
            test_sess['user'] = 'testuser'
        self.assertIn('user', test_sess)

    def test_login_overview(self):
        with self.client:
            with self.client.session_transaction() as session:
                session['user'] = 'testuser'
            response = self.client.get('/overview')
            self.assert200(response)

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=False)
        self.assert_status(response, 302)

    def test_logout_flash(self):
        with self.client.session_transaction() as test_sess:
            test_sess['user'] = 'testuser'
        self.client.get('/logout')
        self.assert_message_flashed("You have been logged out. See you soon!", "notification")

    def test_logout_session(self):
        with self.client:
            with self.client.session_transaction() as test_sess:
                test_sess['user'] = 'testuser'
            self.client.get('/logout')
            with self.client.session_transaction() as test_sess:
                self.assertNotIn('user', test_sess)


if __name__ == "__main__":
    unittest.main()
