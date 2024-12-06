import pandas as pd
import json

restaurants_file = "restaurants.json"
users_file = "sample_users.json"
reviews_file = "sample_reviews.json"

restaurant_ids = []
user_ids = []

with open(restaurants_file, 'r', encoding='utf-8') as file:
    restaurants = json.load(file)

with open(users_file, 'r', encoding='utf-8') as file:
    users = json.load(file)

count = 0

for restaurant in restaurants:
    if count == 100:
        break
    
    restaurant_ids.append(restaurant.get("business_id"))
    count = count + 1

count = 0

for user in users:
    if count == 100:
        break
    
    user_ids.append(user.get("user_id"))
    count = count + 1

print(f"Extracted {len(restaurant_ids)} business IDs")
print(f"Extracted {len(user_ids)} user IDs")

reviews = pd.read_json(reviews_file)
print("Loaded reviews.json")

filtered_reviews1 = reviews[reviews['user_id'].isin(user_ids)]
filtered_reviews2 = filtered_reviews1[filtered_reviews1['business_id'].isin(restaurant_ids)]

filtered_reviews2.to_json('filtered_reviews.json', orient='records', lines=False, force_ascii=False, indent=4)
print(f"Wrote {filtered_reviews2.shape[0]} reviews to filtered_reviews.json")