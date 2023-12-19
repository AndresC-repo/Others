from pydantic import BaseModel


class Settings(BaseModel):
    influxdb_host: str
    influxdb_port: int
    influxdb_user: str
    influxdb_password: str
    influxdb_database: str
    influxdb_measurement_input: str
    influxdb_measurement_prediction: str

    class Config:
        env_file = ".env"
