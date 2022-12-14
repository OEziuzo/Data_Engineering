import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    -this function is responsible for loading the staging tables from the s3
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    -this funtion is responsible for inserting data into the fact and dimension tables from the staging tables
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    -extracts data from the s3, transforms it in the staging table and loads it to the fact and dimension tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()