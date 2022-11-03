
import requests as re
import pandas as pd


# Using the Books API from NY Times: https://developer.nytimes.com/docs/books-product/1/overview

base_url = 'https://api.nytimes.com/svc/books/v3/lists.json'
api_key = 'TPrMxI5GlpSDfhaAgsiEWOnB9mXwlUP7'
api_sk = 'Qb6wxL3blFFOxeIc'

params = {
        'list' : 'hardcover-nonfiction',
        'api-key': 'TPrMxI5GlpSDfhaAgsiEWOnB9mXwlUP7'
    }

response = re.get(base_url, params=params)


print(response.json())

output = response.json()

df = pd.DataFrame.from_dict(output)

print(df)
