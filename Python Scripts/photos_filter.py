import json
import pandas as pd

restaurants_file = "restaurants.json"
photos_file = "photos.json"

restaurant_ids = []
labels = ['outside', 'inside', 'food', 'drinks']

with open(restaurants_file, 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

count = 0

for restaurant in restaurants:
    if count == 100:
        break
    
    restaurant_ids.append(restaurant.get("business_id"))
    count = count + 1

print(f"Extracted {len(restaurant_ids)} business IDs")

df = pd.read_json(photos_file, lines=True)
filter_df = df[df['business_id'].isin(restaurant_ids)]
filter_df = filter_df[filter_df['label'].isin(labels)]
filter_df = filter_df.drop_duplicates(subset='business_id', keep='first')
filter_df.to_json('filtered_photos.json', orient='records', lines=False, force_ascii=False, indent=4)
print(f"Wrote {filter_df.shape[0]} photos to filtered_photos.json")