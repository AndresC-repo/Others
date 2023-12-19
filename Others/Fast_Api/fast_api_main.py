import time
from typing import Any, List

from fastapi import APIRouter, HTTPException, status

from Database.db_main import establish_influxdb_connection

db_connection = establish_influxdb_connection()

# establish a router object for the posts API
router = APIRouter()

######################################################################################
############################### Get all features #####################################
######################################################################################


@router.get("/all/{n_datapoints}", response_model=List[Any])
def retrieve_all_data(n_datapoints: int, measurement: str = db_connection.measurement_input, client: Any = db_connection.get_influxdb_client()):
    """get the latest n_points from all features

    Args:
        n_datapoints (int): how many data points to retrieve

        measurement (str, optional): measurement name. Defaults to input_measurement.

        client (InfluxDBClient, optional): InfluxDB client. Defaults to db_connection.client.


    Returns:
        json: json file containing the datapoints
    """
    try:
        # Construct an InfluxQL query, using format function prevents SQL injection
        query = 'SELECT * FROM {} ORDER BY DESC limit {}'.format(
            measurement, n_datapoints)

        # Query the InfluxDB database
        result = client.query(query)

        # Convert the result to JSON
        json_result = result.get_points()
        print(json_result)

        return json_result

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving data: {str(e)}")


######################################################################################
############################### Get some features ####################################
######################################################################################


@router.get("/someFeatures/{n_datapoints}", response_model=List[Any])
def retrieve_data_1(n_datapoints: int, measurement: str = db_connection.measurement_input, client: Any = db_connection.get_influxdb_client()):
    """get the latest n_points from a spesific feature list

    Args:

        n_datapoints (int): how many data points to retrieve

        measurement (str, optional): measurement name. Defaults to input_measurement.

        client (InfluxDBClient, optional): InfluxDB client. Defaults to db_connection.client.

    Returns:
        json: json file containing the datapoints
    """

    # define feature list
    some_feature_list = ["feature_1", "feature_2", "feature_3, feature_4", "feature_5", "feature_6"]

    try:
        # Construct an InfluxQL query
        query = f'SELECT {", ".join([f"{feature}" for feature in some_feature_list])} FROM {measurement} ORDER BY DESC limit {n_datapoints}'

        # Query the InfluxDB database
        result = client.query(query)

        # Convert the result to python dict
        dict_result = result.get_points()

        return dict_result

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error retrieving data: {str(e)}")

######################################################################################
############################### Get one feature ######################################
######################################################################################


@router.get("/{feature}/{n_datapoints}")
def retrieve_data_2(feature: str, n_datapoints: int, client: Any = db_connection.get_influxdb_client()):
    """get the latest n_points from a spesific feature

    Args:
        feature (str): feature name

        n_datapoints (int): how many data points to retrieve

        client (InfluxDBClient, optional): InfluxDB client. Defaults to db_connection.client.
    Returns:
        json: json file containing the datapoints
    """
    try:
        # Construct an InfluxQL query
        query = 'SELECT {} FROM dataset_1 ORDER BY DESC limit {}'.format(
            feature, n_datapoints)

        # Query the InfluxDB database
        result = client.query(query)

        # Convert the result to JSON
        json_result = result.get_points()

        return json_result

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving data: {str(e)}")

######################################################################################
############################### Inject Predictions ###################################
######################################################################################


@router.post("/{prediction_measurement}/{prediction_value}/{timestamp}")
def inject_prediction(prediction_measurement: str, prediction_value: float, timestamp: str, client: Any = db_connection.get_influxdb_client()):
    """
    Inject predictions and timedata(timestamp) again to a spesific measurment table in the predictions database
    This is done by creating datapoints first that needed to be injected, then injecting them using the influxdb client.
    parameters:
    
    Args:
        prediction_measurement (str): name of the measurement table whee the predictions are to be stored

        prediction_value (float): prediction value to be injected in DB

        timestamp (str): timestamp of the prediction

        client (InfluxDBClient): InfluxDB client. Defaults to db_connection.client.


    Returns:
        None
    """

    # create prediction datapoint
    prediction_point = {
        "measurement": prediction_measurement,
        "tags": "",  # tags can be provided but no really needed
        # take the only element in prediction list
        "fields": dict(prediction=prediction_value, time=timestamp)
    }

    # inject datapoints using the influxdb client
    client.write_points(points=[prediction_point], time_precision='s')
