import pymongo

def connect_to_mongodb(database_name, collection_name):
    try:
        mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        mongo_db = mongo_client[database_name]
        mongo_collection = mongo_db[collection_name]
        return mongo_collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return None

def find_top_products_by_quantity_sold(collection, limit=10):
    try:
        top_products = collection.find().sort("all_time_quantity_sold", pymongo.DESCENDING).limit(limit)
        return top_products
    except Exception as e:
        print(f"Error finding top products by quantity sold: {str(e)}")
        return []

def find_top_products_by_rating_average(collection, limit=10):
    try:
        top_products = collection.find().sort("rating_average", pymongo.DESCENDING).limit(limit)
        return top_products
    except Exception as e:
        print(f"Error finding top products by rating average: {str(e)}")
        return []

def find_top_products_by_lowest_price(collection, limit=10):
    try:
        query = {"price": {"$ne": 0}}
        top_products = collection.find(query).sort("price", pymongo.ASCENDING).limit(limit)
        return top_products
    except Exception as e:
        print(f"Error finding top products by lowest price: {str(e)}")
        return []

def write_products_to_file(products, result_filename):
    try:
        with open(result_filename, "w", encoding="utf-8") as file:
            for index, product in enumerate(products, start=1):
                product_name = product.get("name", "")
                price = product.get("price", 0)
                url = product.get('short_url', "")
                Quantity_sold = product.get('all_time_quantity_sold',0)
                rating = product.get('rating_average',0)
                file.write(f"{index}. Product: {product_name}\n    ShortUrl: {url}\n    Quantity sold: {Quantity_sold}\n    Average Rating: {rating}\n   Price: {price}\n\n")
        print(f"Results written to {result_filename}")
    except Exception as e:
        print(f"Error writing to file: {str(e)}")

def main():
    # Connect to MongoDB
    mongo_collection = connect_to_mongodb("Tikidata", "final_data")
    if mongo_collection is not None:

        # Find and write top products by quantity sold
        print("Finding top products by quantity sold...")
        top_quantity_sold_products = find_top_products_by_quantity_sold(mongo_collection)
        write_products_to_file(top_quantity_sold_products, "task4.3_top_products_sold.txt")
        print("Top products by quantity sold written to file.")

        # Find and write top products by rating average
        print("Finding top products by rating average...")
        top_rated_products = find_top_products_by_rating_average(mongo_collection)
        write_products_to_file(top_rated_products, "task4.3_top_rated_products.txt")
        print("Top rated products written to file.")

        # Find and write top products by lowest price
        print("Finding top products by lowest price...")
        top_lowest_price_products = find_top_products_by_lowest_price(mongo_collection)
        write_products_to_file(top_lowest_price_products, "task4.3_top_lowest_price_products_with_url.txt")
        print("Top lowest price products written to file.")

if __name__ == "__main__":
    main()
