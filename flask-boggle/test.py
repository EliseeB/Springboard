from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Set up the test environment before each test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test the homepage to ensure session data and HTML content are as expected."""

        with self.client:
            response = self.client.get('/')
            # Ensure 'board' is in the session
            self.assertIn('board', session)
            # Ensure 'highscore' and 'nplays' are initially None
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            # Check if certain HTML content is present in the response
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if a word is valid by modifying the board in the session."""

        with self.client as client:
            with client.session_transaction() as sess:
                # Modify the 'board' in the session
                sess['board'] = [["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=cat')
        # Check if the response result is 'ok'
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test if a word is not on the board."""

        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        # Check if the response result is 'not-on-board'
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if a word is not in the dictionary."""

        self.client.get('/')
        response = self.client.get(
            '/check-word?word=fsjdakfkldsfjdslkfjdlksf')
        # Check if the response result is 'not-word'
        self.assertEqual(response.json['result'], 'not-word')
