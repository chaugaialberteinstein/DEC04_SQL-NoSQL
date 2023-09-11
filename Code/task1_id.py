import requests
import time
import random
import pandas as pd

# Read the categories from the CSV file
df = pd.read_csv('CateList.csv')
categories_id = df['LEAF_CAT_ID'][0:2311]  # Modify the range as needed

# Define headers for the requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Iterate through categories
for category in categories_id:
    category = category.strip('c')
    print('Run request for category', category)
    
    url = "https://tiki.vn/api/v2/products"
    product_id = []
    params = {
        'limit': '40',
        'aggregations': '2',
        'category': category,
        'page': 1
    }


    while True:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            print('Request success for category', category)
            try:
                data = response.json().get('data')
                if not data:
                    break  # Exit the loop when there are no more products
                for record in data:
                    product_id.append({'id': record.get('id')})
            except KeyError as e:
                print("KeyError:", e)  # Print a helpful error message
            except Exception as e:
                print("An unexpected error occurred:", e)  # Catch other exceptions

            params['page'] += 1  # Move to the next page
            time.sleep(random.uniform(3, 5))
            
        else:
            print('Failed to fetch data. Status code:', response.status_code)
            print(response.text)
            time.sleep(random.uniform(3, 5))

# Create a DataFrame from the collected product IDs and save to CSV
df = pd.DataFrame(product_id)
df.to_csv('Task1_id.csv', index=False)


