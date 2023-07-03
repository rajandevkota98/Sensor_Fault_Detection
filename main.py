from sensor.configuration.mongodb_connection import MongoDBClient

from sensor.exception import SensorException
from sensor.logger import logging
import os, sys

def test_exception():
    try:
        logging.info('into the try block')
        x = 5
        y = 0
        return  x/y
    except Exception as e:
        raise SensorException(e,sys)
    
if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        raise SensorException(e,sys)
