import os
import glob
import pandas as pd
from sqlalchemy import create_engine

# pkl files directory
PKL_DIR = '/opt/airflow/data' 

# connections config
DB_USER = 'airflow'
DB_PASSWORD = 'airflow'
DB_HOST = 'postgres'
DB_PORT = '5432'
DB_NAME = 'airflow'
DB_TABLE = 'transactions'

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
    df = load_all_pickles(PKL_DIR)
    insert_into_postgres(df)

if __name__ == '__main__':
    main()