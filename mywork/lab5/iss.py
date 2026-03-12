import os
from datetime import datetime

import mysql.connector
import requests

API_URL = "http://api.open-notify.org/iss-now.json"

REPORTER_ID = "sgm3pm"
REPORTER_NAME = "Hermela"


def extract():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def transform(data):
    return {
        "message": data["message"],
        "latitude": round(float(data["iss_position"]["latitude"]), 4),
        "longitude": round(float(data["iss_position"]["longitude"]), 4),
        "timestamp": datetime.utcfromtimestamp(data["timestamp"]).strftime("%Y-%m-%d %H:%M:%S"),
        "reporter_id": REPORTER_ID,
    }


def register_reporter(table, reporter_id, reporter_name):
    db = None
    cursor = None

    try:
        db = mysql.connector.connect(
            host=os.environ["DBHOST"],
            user=os.environ["DBUSER"],
            password=os.environ["DBPASS"],
            database="iss",
        )
        cursor = db.cursor()

        check_sql = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(check_sql, (reporter_id,))
        existing = cursor.fetchone()

        if existing is None:
            insert_sql = f"""
                INSERT INTO {table} (reporter_id, reporter_name)
                VALUES (%s, %s)
            """
            cursor.execute(insert_sql, (reporter_id, reporter_name))
            db.commit()
            print(f"Registered reporter: {reporter_id}")
        else:
            print(f"Reporter {reporter_id} already exists.")

    except mysql.connector.Error as e:
        print(f"Database error in register_reporter: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


def load(record):
    db = None
    cursor = None

    try:
        db = mysql.connector.connect(
            host=os.environ["DBHOST"],
            user=os.environ["DBUSER"],
            password=os.environ["DBPASS"],
            database="iss",
        )
        cursor = db.cursor()

        insert_sql = """
            INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            record["message"],
            record["latitude"],
            record["longitude"],
            record["timestamp"],
            record["reporter_id"],
        )

        cursor.execute(insert_sql, values)
        db.commit()
        print("Inserted ISS location successfully.")

    except mysql.connector.Error as e:
        print(f"Database error in load: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


def main():
    register_reporter("reporters", REPORTER_ID, REPORTER_NAME)
    data = extract()
    record = transform(data)
    load(record)
    print(record)


if __name__ == "__main__":
    main()