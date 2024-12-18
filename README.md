### Overview

The MovieQuotes library is a lightweight Python library designed to generate and manage famous movie quotes. It provides functionality to fetch random quotes, search quotes by movie titles, add new quotes, and list all stored quotes. This is a simple tool for entertainment, this library makes working with movie quotes fun and easy.

### Features
1. Get Random Quote: Fetch a random quote from the predefined database.
2. Search Quotes by Movie: Find quotes from a specific movie.
3. Add Custom Quotes: Expand the quote database with your own favorite quotes.
4. List All Quotes: View the entire collection of stored quotes.

### Installation

 To install do **pip install moviequote-generator** 

### Usage

from moviequote_generator.core import MovieQuotes

1. Fetch a random quote

random_quote = quotes.get_random_quote()
print(f'"{random_quote["quote"]}" - {random_quote["movie"]}')

2. Search for a Quote by Movie

movie_title = "The Terminator"
quote = quotes.get_quote_by_movie(movie_title)
if isinstance(quote, list):
    for q in quote:
        print(f'"{q["quote"]}" - {q["movie"]}')
else:
    print(quote)  # Handles "No quotes found" case

3. Add a New Quote

quotes.add_quote("I'm walking here!", "Midnight Cowboy")
print("New quote added successfully!")

4. List All Quotes

quotes_list = quotes.list_quotes()
for q in quotes_list:
    print(f'"{q["quote"]}" - {q["movie"]}')