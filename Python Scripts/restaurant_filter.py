import pandas as pd
import re

business = pd.read_json('businesses.json', lines=True)

business['restaurant'] = business['categories'].str.contains(pat='Restaurant', flags=re.IGNORECASE, regex=True, na=False)
business['food'] = business['categories'].str.contains(pat='Food', flags=re.IGNORECASE, regex=True, na=False)

restaurants = business[(business['restaurant']) | (business['food'])]
restaurants = restaurants.drop(['restaurant', 'food'], axis=1)

ca_restaurants = restaurants[restaurants['state'] == 'CA']

open_restaurants = ca_restaurants[ca_restaurants['is_open'] == 1]
open_restaurants.to_json('restaurants.json', orient='records', lines=False, force_ascii=False, indent=4)
print(f"Wrote {open_restaurants.shape[0]} restaurants to restaurants.json")