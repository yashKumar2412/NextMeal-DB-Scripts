import psycopg2
import json

conn = psycopg2.connect(
    dbname="nextmeal_db",
    user="postgres",
    password="nextmeal123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

with open("sample_users.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for record in data:
    cursor.execute(
        """
        INSERT INTO users (
            user_id, name, review_count, yelping_since, useful, funny, cool
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """,
        (
            record["user_id"],
            record["name"],
            record["review_count"],
            record["yelping_since"],
            record["useful"],
            record["funny"],
            record["cool"]
        )
    )

conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")