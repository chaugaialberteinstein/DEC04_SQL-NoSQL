import pymongo
import csv
import matplotlib.pyplot as plt

# MongoDB connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Tikidata"]
mongo_collection = mongo_db["final_data"]

# Dictionary to store origin counts
origin_counts = {}

try:
    for index, document in enumerate(mongo_collection.find({}), start=1):
        print(f"Processing product {index}")
        
        try:
            specification = document.get("specifications", [])

            for spec_item in specification:
                attributes = spec_item.get("attributes", [])

                for attribute in attributes:
                    if attribute.get("code") == "origin":
                        origin_value = attribute.get("value", "").strip()

                        if origin_value:
                            if origin_value in origin_counts:
                                origin_counts[origin_value] += 1
                            else:
                                origin_counts[origin_value] = 1
        except Exception as e:
            print(f"Error processing product {index}: {str(e)}")

finally:
    # Close MongoDB connection
    mongo_client.close()

# Save origin counts to a CSV file
csv_filename = "task4.2_origin_counts.csv"
try:
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Origin", "Count"])
        for origin, count in origin_counts.items():
            csv_writer.writerow([origin, count])
    print(f"Origin counts written to {csv_filename}")
except Exception as e:
    print(f"Error writing origin counts to CSV: {str(e)}")
