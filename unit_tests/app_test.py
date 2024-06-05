import unittest
from flask_testing import TestCase
from app import app

class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.secret_key = 'test_key'
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_template_rendered(self):
        response = self.client.get('/')
        self.assert_template_used('mood.html')

    def test_template_rendered_quote(self):
        response = self.client.get('/quote')
        self.assert_template_used('quote.html')

    def test_form_submission_wrongpw(self): # check password validaiton and flash messages
        response = self.client.post('/register', data={'FirstName': 'Rachel', 'LastName': 'Tookey', "Username": "Rachel1993", "email": "rachel@tookey.com", "password":"snow", "confirm":"rain", "accept_tos":True})
        self.assert_message_flashed('Password and Password Confirmation do not match', "error")

    def test_overview_redirect(self): # check it redirects if not logged in
        response = self.client.get('/overview')
        self.assert_status(response, 302)

    def test_200(self): # check it redirects if not logged in
        response = self.client.post('/register', data={'FirstName': 'Rachel', 'LastName': 'Tookey', "Username": "Rachel1993", "email": "rachel@tookey.com", "password":"snow", "confirm":"snow", "accept_tos":True})
        self.assert200(response)

    def test_404(self):
        response = self.client.get('/hello')
        self.assert404(response)

    def test_login_logic(self):
        response = self.client.get('/overview')
        self.assert_status(response, 302)

        response = self.client.get('/login')
        self.assert_status(response, 200)

        with self.client.session_transaction() as test_sess:
            test_sess['user'] = 'testuser'

        response = self.client.get('/overview')
        self.assert200(response)

    def test_logout_logic(self):
        response = self.client.get('/logout')
        self.assert_status(response, 302)

        with self.client.session_transaction() as test_sess:
            self.assertNotIn('user', test_sess)

if __name__ == "__main__":
    unittest.main()
