import sqlalchemy
import pandas as pd

# Define the database connection URL
db_url = "mysql://root:123456@localhost/tikidata"

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(db_url)

# Define your SQL query
query = "SELECT category_id, COUNT(*) as product_count FROM final GROUP BY category_id"

# Execute the query and fetch the results into a DataFrame
df = pd.read_sql(query, con=engine)

# Close the database connection
engine.dispose()

# Read the "CateList.csv" file
csv_df = pd.read_csv('CateList.csv')

# Extract the 'LEAF_CAT_ID' column and strip 'c' from its values
csv_df['LEAF_CAT_ID'] = csv_df['LEAF_CAT_ID'].str.lstrip('c')

# Convert the 'LEAF_CAT_ID' column to integers
csv_df['LEAF_CAT_ID'] = pd.to_numeric(csv_df['LEAF_CAT_ID'], errors='coerce')

# Filter the DataFrame to include only matching category IDs
matching_df = df[df['category_id'].isin(csv_df['LEAF_CAT_ID'])]

# Save the matching results to a CSV file
matching_df.to_csv('Task4.1_CategoriesId_product_counts.csv', index=False)
