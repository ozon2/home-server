# The script needs to be run as root to be able to access the sensor.

import time
import os
import board
import adafruit_dht
from influxdb_client import Point, InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

dhtDevice = adafruit_dht.DHT22(board.D4)

client = InfluxDBClient(url=os.getenv('INFLUXDB_URL'), org="home", token=f"{os.getenv('INFLUXDB_CLIENT_USER')}:{os.getenv('INFLUXDB_CLIENT_PASSWORD')}")
write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))

        p = Point("dht").field("temperature", temperature_c).field("humidity", humidity).tag("id", "1")
        write_api.write(bucket="sensors", record=p)

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2)
        continue

    except KeyboardInterrupt as error:
        dhtDevice.exit()
        raise error

    except Exception as error:
        print(error)

    time.sleep(60)
