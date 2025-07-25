import os
from dotenv import load_dotenv
load_dotenv()
import pymysql
from pymysql.cursors import DictCursor

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "db": os.getenv("DB_NAME"),
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}

def db_connection():
    return pymysql.connect(**db_config)

def run_sql(sql, params=None, fetchone=False, fetchmany=False, return_id=False):
    # return None
    with db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()
            if return_id:
                return  cursor.lastrowid
            if fetchone:
                return cursor.fetchone()
            if fetchmany:
                return cursor.fetchmany(size=fetchmany)
            return cursor.fetchall()
