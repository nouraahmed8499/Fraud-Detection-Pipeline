import os
import glob
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

# pkl files directory
PKL_DIR = '/opt/airflow/data' 

# connections config
DB_USER = 'airflow'
DB_PASSWORD = 'airflow'
DB_HOST = 'postgres'
DB_PORT = '5432'
DB_NAME = 'fraud-detection'
DB_TABLE = 'transactions'
DEFAULT_DB = 'postgres'

def create_database_if_not_exists():
    """
    Connects to the default DB and creates the target DB if it does not exist.
    """
    conn = psycopg2.connect(
        dbname=DEFAULT_DB,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cur.fetchone()

    if not exists:
        cur.execute(f"CREATE DATABASE \"{DB_NAME}\"")
        print(f"Database '{DB_NAME}' created.")
    else:
        print(f"Database '{DB_NAME}' already exists.")

    cur.close()
    conn.close()

    
def load_all_pickles(pkl_dir):
    """
    Load and combine all .pkl files in the specified directory
    Parameters:
        pkl_dir (str): Path to the folder containing .pkl files
    Returns:
        pandas.DataFrame: A single DataFrame containing all rows from the .pkl files
    Raises:
        FileNotFoundError: If no .pkl files are found
    """

    pkl_files = glob.glob(os.path.join(pkl_dir, '*.pkl'))
    if not pkl_files:
        raise FileNotFoundError(f"No .pkl files found in {pkl_dir}")

    dfs = [pd.read_pickle(file) for file in pkl_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    print(f"Loaded {len(dfs)} pickle files with {combined_df.shape[0]} total rows.")
    return combined_df

def insert_into_postgres(df):
    """Insert DataFrame into PostgreSQL table using SQLAlchemy
    Parameters:
        df (pandas.DataFrame): Data to insert into the database
    """
    conn_str = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(conn_str)
    

    # Write to PostgreSQL
    df.to_sql(DB_TABLE, engine, if_exists='replace', index=False)
    print(f"Data inserted into PostgreSQL table '{DB_TABLE}' ({df.shape[0]} rows)")

def main():
    """
    main function to load .pkl files and insert into PostgreSQL
    """
    create_database_if_not_exists()
    df = load_all_pickles(PKL_DIR)
    insert_into_postgres(df)

if __name__ == '__main__':
    main()