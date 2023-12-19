from decouple import UndefinedValueError, config
from influxdb.client import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError


class InfluxdbDatabase:
    """
    A class for connecting to and managing an InfluxDB database.

    Attributes:
        host (str): The InfluxDB server host.
        port (int): The InfluxDB server port.
        user (str): The username for authentication.
        password (str): The password for authentication.
        database (str): The name of the InfluxDB database.
        client (InfluxDBClient): The InfluxDB client for database interactions.

    """
    ############### __init__ ###############################

    def __init__(self):
        """
        Initialize InfluxDB client and credentials.
        """

        self.client: InfluxDBClient = None
        self.host: str = None
        self.port: int = None
        self.user: str = None
        self.password: str = None
        self.database: str = None
        self.measurement_input = None
        self.measurement_prediction = None
        self.set_influxdb_credentials()

        print(self.host)
        print(self.port)

    ############### set_influxdb_credentials ###################

    def set_influxdb_credentials(self):
        """
        Get InfluxDB credentials from environment variables.
        """
        try:

            self.host = config('INFLUXDB_HOST')
            self.port = config('INFLUXDB_PORT')
            self.user = config('INFLUXDB_USER')
            self.password = config('INFLUXDB_PASSWORD')
            self.database = config('INFLUXDB_DATABASE')
            self.measurement_input = config('INFLUXDB_MEASUREMENT_INPUT')
            self.measurement_prediction = config(
                'INFLUXDB_MEASUREMENT_PREDICTION')

        except UndefinedValueError as e:
            raise EnvironmentError(
                f"Error reading configuration from .env file: {e}")

        print("InfluxDB Credentials:", self.host, self.port,
              self.user, self.password, self.database)

    ############### connect_to_influxdb #######################
    def connect_to_influxdb(self):
        """
        Establish a connection to InfluxDB.

        Returns:
            InfluxDBClient: The InfluxDB client for database interactions.
        """
        try:
            self.client = InfluxDBClient(
                host=self.host,
                port=self.port,
                username=self.user,
                password=self.password,
                database=self.database
            )

            # Test connection
            self.client.ping()
            print("Connected to InfluxDB")

        except InfluxDBClientError as e:
            print(f"Error connecting to InfluxDB: {e}")

    ############### get_influxdb_client ######################
    def get_influxdb_client(self):
        """
        Get the InfluxDB client.

        Returns:
            InfluxDBClient: The InfluxDB client for database interactions.
        """
        return self.client

    ############### close_connection #########################

    def close_connection(self):
        """
        Close the connection to InfluxDB.
        """
        self.client.close()
        print("Connection closed")
