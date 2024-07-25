import sqlite3
import csv


csv_file_path = 'Spotify.csv'
db_file_path = 'Spotify.db'
table_name = 'Spotify'

# Connect to the SQLite database 
conn = sqlite3.connect(db_file_path)
cur = conn.cursor()

# Function to create table based on CSV header
def create_table_from_csv(file_path, table_name, encoding='utf-8'):
    with open(file_path, newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        columns = ', '.join([f'"{header}" TEXT' for header in headers])
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')

# Function to import CSV data into the table
def import_csv_to_table(file_path, table_name, encoding='utf-8'):
    with open(file_path, newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        placeholders = ', '.join(['?' for header in headers])
        for row in reader:
            cur.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)

# Create table and import data
create_table_from_csv(csv_file_path, table_name, encoding='latin1')  
import_csv_to_table(csv_file_path, table_name, encoding='latin1')    

# Commit and close the connection
conn.commit()
conn.close()

print(f"CSV data has been successfully imported into the '{table_name}' table in the database '{db_file_path}'.")
