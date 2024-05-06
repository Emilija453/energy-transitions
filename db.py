import sqlite3
import pandas as pd
import os

conn = sqlite3.connect('energy.db')
csv_dir = 'data'

# List of CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

for csv_file in csv_files:
    # Name the table
    table_name = os.path.splitext(csv_file)[0]
    
    # CSV to pd
    print(f"Reading CSV file '{csv_file}'...")
    df = pd.read_csv(os.path.join(csv_dir, csv_file))
    
    # pd to SQLite
    print(f"Writing data from CSV file '{csv_file}' to SQLite table '{table_name}'.")
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data from CSV file '{csv_file}' successfully written to SQLite table '{table_name}'.")
    
conn.close()
