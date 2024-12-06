import os
import json
import boto3

bucket_name = "restaurant-photos"

photos_folder = "photos/"
filtered_photos_file = "filtered_photos.json"

with open(filtered_photos_file, "r", encoding="utf-8") as f:
    filtered_photos = json.load(f)

s3 = boto3.client("s3")

for photo in filtered_photos:
    photo_id = photo["photo_id"]
    photo_file = os.path.join(photos_folder, f"{photo_id}.jpg")
    
    if os.path.exists(photo_file):
        try:
            s3.upload_file(photo_file, bucket_name, f"photos/{photo_id}.jpg")
            print(f"Uploaded {photo_id}.jpg to S3 successfully.")
        except Exception as e:
            print(f"Error uploading {photo_id}.jpg: {e}")
    else:
        print(f"Photo file not found: {photo_file}")