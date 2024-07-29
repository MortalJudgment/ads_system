import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dotenv import load_dotenv
import json
from database.db_connection import create_admin_db_connection, table_exists, get_table_info

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

def insert_ad_data(data, db_connection):
    conn = db_connection.get_connection()
    cursor = conn.cursor()
    for ad in data:
        cursor.execute(
            """
            INSERT INTO ads (ad_id, field, advertiser, ad_name, ad_description, ad_image, ad_url, target_audience, bid)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                ad['Ad ID'],
                ad['Field'],
                ad['Advertiser'],
                ad['Ad Name'],
                ad['Ad Description'],
                ad['Ad Image'],
                ad['Ad URL'],
                ad['Target Audience'],
                ad['Bid']
            )
        )
    conn.commit()
    cursor.close()
    db_connection.release_connection(conn)

def query_ads_table(db_connection):
    conn = db_connection.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ads;")
    rows = cursor.fetchall()
    cursor.close()
    db_connection.release_connection(conn)
    return rows

def main():
    # Read the JSON file with UTF-8 encoding
    json_file_path = os.path.join(os.path.dirname(__file__), 'data_ads.json')
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create admin database connection
    db_connection = create_admin_db_connection()

    # Check if the 'ads' table exists
    if not table_exists(db_connection, 'ads'):
        print("Table 'ads' does not exist. Please create the table first.")
        return

    # Get table information
    table_info = get_table_info(db_connection, 'ads')
    print("Table 'ads' information:")
    for column_name, data_type in table_info:
        print(f"Column: {column_name}, Data Type: {data_type}")

    # Insert data into the database
    insert_ad_data(data, db_connection)

    # Query the 'ads' table to see the data
    ads_data = query_ads_table(db_connection)
    print("\nData in 'ads' table:")
    for row in ads_data:
        print(row)

if __name__ == "__main__":
    main()