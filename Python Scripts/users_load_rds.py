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

JSON_FILE_PATH = "sample_users.json"

def insert_users():
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
            users = json.load(file)

        for user in users:
            cursor.execute(
                """
                INSERT INTO users (
                    user_id, name
                )
                VALUES (%s, %s);
                """,
                (
                    user.get("user_id"),
                    user.get("name")
                )
            )

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

if __name__ == "__main__":
    insert_users()