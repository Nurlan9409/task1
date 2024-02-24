import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database='example',
            host='localhost',
            user='postgres',
            password='3110'
        )

        cursor = database.cursor()
        cursor.execute(query)
        query_data = ["insert", "create", "delete"]
        if query_type in query_data:
            database.commit()

            if query_type == "insert":
                return "Inserted"

            elif query_type == "create":
                return "Created"

            elif query_type == "delete":
                return "Deleted"

        else:
            return cursor.fetchall()


