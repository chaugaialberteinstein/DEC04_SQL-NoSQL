import pymongo
from bs4 import BeautifulSoup
import mysql.connector

try:
    # MongoDB connection
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_db = mongo_client["Tikidata"]
    mongo_collection = mongo_db["final_data"]

    # MySQL connection
    mysql_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="tikidata"
    )
    mysql_cursor = mysql_connection.cursor()

    # Extract data from MongoDB and insert into MySQL
    for product_data in mongo_collection.find():
        try:
            # Extract relevant information from product_data
            product_name = product_data.get('name', '')
            short_description = product_data.get('short_description', '')
            description = product_data.get('description', '')
            description = BeautifulSoup(description, 'html.parser').get_text()  # Remove HTML tags
            url = product_data.get('short_url', '')
            rating_average = product_data.get('rating_average', 0)
            quantity_sold = product_data.get('all_time_quantity_sold', 0)
            price = product_data.get('price', 0)
            categories = product_data.get('categories', {})
            category_id = categories.get('id', 0)
            day_ago_created = product_data.get('day_ago_created', '')
            print(f"Inserting product: {product_name}")

            # Insert data into MySQL
            mysql_cursor.execute(
                "INSERT INTO final (product_name, short_description, description, url, rating, sold_quantity, price, category_id, day_ago_created) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (product_name, short_description, description, url, rating_average, quantity_sold, price, category_id, day_ago_created)
            )
            mysql_connection.commit()
        except Exception as e:
            print(f"Error while processing MongoDB data: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close MySQL cursor and connection
    if mysql_cursor:
        mysql_cursor.close()
    if mysql_connection:
        mysql_connection.close()

    # Close MongoDB connection
    if mongo_client:
        mongo_client.close()