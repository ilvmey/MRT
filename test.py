import psycopg2
import os

DB_NAME = os.getenv('POSTGRES_NAME', 'mrt')
DB_USER = os.getenv('POSTGRES_USER', 'mrt')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mrt')
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port='5432'
    )
    print("连接成功")
except Exception as e:
    print(f"连接失败: {e}")
finally:
    if conn:
        conn.close()
