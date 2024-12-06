import psycopg2
import json
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")

JSON_FILE_PATH = "restaurants.json"

def insert_restaurants():

    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()
        print("Connected to the database successfully!")

        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as file:
            restaurants = json.load(file)
        
        count = 0

        for restaurant in restaurants:

            if count == 100:
                break   

            categories = restaurant.get("categories")
            if categories:
                categories_array = "{" + ",".join(categories.split(", ")) + "}"  # Convert to array
            else:
                categories_array = None    
            
            cursor.execute(
                """
                INSERT INTO restaurants (
                    name, address, city, state, postal_code, latitude, longitude,
                    average_rating, review_count, is_open, categories, hours, business_id, attributes
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    restaurant.get("name"),
                    restaurant.get("address"),
                    restaurant.get("city"),
                    restaurant.get("state"),
                    restaurant.get("postal_code"),
                    restaurant.get("latitude"),
                    restaurant.get("longitude"),
                    restaurant.get("stars"),
                    restaurant.get("review_count"),
                    bool(restaurant.get("is_open")),
                    categories_array,
                    json.dumps(restaurant.get("hours")),
                    restaurant.get("business_id"),
                    json.dumps(restaurant.get("attributes")),
                )
            )
            print("Inserted " + str(count))
            count = count + 1

        # Commit changes
        conn.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the connection
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

# Run the script
if __name__ == "__main__":
    insert_restaurants()