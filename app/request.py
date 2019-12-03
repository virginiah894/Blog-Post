import requests
from app. config import Config
from .models import Quote

quote_api = Config.QUOTE_API

def display_quote():
  find_quote = requests.get(quote_api)
  get_new_quote = find_quote.json()
  author = get_new_quote.get("author")
  quote = get_new_quote.get("quote")
  permalink = get_new_quote.get("permalink")
  quote_object = Quote(author,quote,permalink)
  return quote_object
