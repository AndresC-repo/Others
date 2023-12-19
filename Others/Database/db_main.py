import time

from InfluxDB_model import InfluxdbDatabase


def establish_influxdb_connection():
    while True:
        try:
            db_connection = InfluxdbDatabase()
            db_connection.connect_to_influxdb()
            break

        except Exception as e:
            print("Error connecting to InfluxDB: ", str(e))
            print("Retrying in 2 seconds.....")
            time.sleep(2)
            continue
    return db_connection

# Example usage
db_connection = establish_influxdb_connection()