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

with open("restaurants.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for record in data:
    cursor.execute(
        """
        INSERT INTO restaurants (
            business_id, name, address, city, state, postal_code, latitude, longitude, stars,
            review_count, attributes, categories, hours
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (
            record["business_id"],
            record["name"],
            record["address"],
            record["city"],
            record["state"],
            record["postal_code"],
            record["latitude"],
            record["longitude"],
            record["stars"],
            record["review_count"],
            json.dumps(record["attributes"]),
            record["categories"],
            json.dumps(record["hours"]),
        )
    )

conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")