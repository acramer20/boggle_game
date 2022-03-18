from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def setUp(self):
        """To do before each test"""
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_homepage(self):
        """Saving info to session and HTML is showing up"""
        response = self.client.get('/')
        self.assertIn('board', session)
        self.assertIsNone(session.get('highscore'))
        self.assertIsNone(session.get('num_plays'))
        
    def test_valid_word(self):
        """Test if the word is valid depending on the board"""
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["D","O","G","G","G"],["D","O","G","G","G"],["D","O","G","G","G"],["D","O","G","G","G"],["D","O","G","G","G"]]
        response = self.client.get('/check-word?word=dog')
        self.assertEqual(response.json['result'], 'ok')
    
    def test_invalid_word(self):
        """testing if the word is in the dictionary but not on board"""
        self.client.get('/')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_non_english_word(self):
        """testing to for a made up word"""
        self.client.get('/')
        response = self.client.get('/check-word?word=sdjknsjalbvsjhdfv')
        self.assertEqual(response.json['result'],'not-word')

    
