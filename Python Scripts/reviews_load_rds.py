import boto3
import json
from decimal import Decimal
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
REVIEWS_TABLE = os.getenv("REVIEWS_TABLE")

dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

json_file_path = 'filtered_reviews.json'

table = dynamodb.Table(REVIEWS_TABLE)

with open(json_file_path, "r", encoding="utf-8") as f:
    reviews = json.load(f)

for review in reviews:
    try:
        response = table.put_item(Item=review)
        print(f"Successfully added review: {review['review_id']}")
    except Exception as e:
        print(f"Error adding review {review['review_id']}: {e}")