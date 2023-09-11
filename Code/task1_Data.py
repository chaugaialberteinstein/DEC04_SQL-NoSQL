import requests
import time
from pymongo import MongoClient, errors
import pandas as pd
import requests
import time


# Read data from the CSV file
data = pd.read_csv('Task1_id.csv')

# Extract unique product IDs from the 'id' column
product_ids = data['id'].unique()


def insert_data(collection, data):
    try:
        collection.insert_one(data)
        print('Data inserted successfully.')
    except errors.DuplicateKeyError:
        print('Duplicate data found. Skipping insertion.')

def collect_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    # Create a list of URLs using the unique product IDs
    urls = ['https://tiki.vn/api/v2/products/{}'.format(product_id) for product_id in product_ids]


    # Initialize a MongoDB client and collection
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Tikidata"]
    collection = db["final_data"]    

    for i, product_id in enumerate(product_ids):
        url = 'https://tiki.vn/api/v2/products/{}'.format(product_id)
        sent_request = requests.get(url=url, headers=headers)

        if sent_request.status_code == 200:
            try:
                product_data = sent_request.json()
            except:
                with open('id_error.txt', 'a') as file:
                    file.write(str(product_id).strip('\n'))
                    file.write('\n')
                time.sleep(10)
            else:
                insert_data(collection, product_data)
                print('Crawl data for product_id {} success !!!'.format(product_id))
                with open('id_running.txt', 'w') as file:
                    file.write(str(product_id).strip('\n'))
                    file.write('\n')
        else:
            with open('id_error.txt', 'a') as file:
                file.write(str(product_id).strip('\n'))
                file.write('\n')

        if i % 100 == 0:
            print('Products collected: {}'.format(i))

if __name__ == '__main__':
    collect_data()
