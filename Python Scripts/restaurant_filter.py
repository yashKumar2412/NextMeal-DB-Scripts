import pandas as pd
import re

business = pd.read_json('businesses.json', lines=True)

business['restaurant'] = business['categories'].str.contains(pat='Restaurant', flags=re.IGNORECASE, regex=True, na=False)
business['food'] = business['categories'].str.contains(pat='Food', flags=re.IGNORECASE, regex=True, na=False)

restaurants = business[(business['restaurant']) | (business['food'])]
restaurants = restaurants.drop(['restaurant', 'food'], axis=1)

US_STATES = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 
    'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 
    'VA', 'WA', 'WV', 'WI', 'WY'
]
us_restaurants = restaurants[restaurants['state'].isin(US_STATES)]

open_restaurants = us_restaurants[us_restaurants['is_open'] == 1]
open_restaurants.to_json('restaurants.json', orient='records', lines=False, force_ascii=False, indent=4)
print(f"Wrote {restaurants.shape[0]} restaurants to restaurants.json")