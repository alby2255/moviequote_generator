import unittest
from movie_quotes.core import MovieQuotes

class TestMovieQuotes(unittest.TestCase):
    def setUp(self):
        self.quotes = MovieQuotes()

    def test_random_quote(self):
        quote = self.quotes.get_random_quote()
        self.assertIn("quote", quote)
        self.assertIn("movie", quote)

    def test_get_quote_by_movie(self):
        quotes = self.quotes.get_quote_by_movie("Star Wars")
        self.assertGreaterEqual(len(quotes), 1)

    def test_add_quote(self):
        self.quotes.add_quote("This is a test quote.", "Test Movie")
        quotes = self.quotes.get_quote_by_movie("Test Movie")
        self.assertGreaterEqual(len(quotes), 1)
