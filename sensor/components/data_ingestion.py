from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from pandas import DataFrame
from sensor.data_access.sensor_data import SensorData


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
        
    def export_data_into_feature_store(self,)->DataFrame:
        """
        Export the mongodb data into  the feature store folder
        """
        try:
            logging.info('Extracting the data from mongodb to feature store')
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(collection_name='car')
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok= True)
            dataframe.to_csv(feature_store_file_path,index = False,header = True)
            return dataframe


        except Exception as e:
            raise SensorException(e,sys)


    def split_data_as_train_test(self, dataframe:DataFrame):
        """
        Split the data into test data ans train data
        """
        pass


    def initiate_data_ingestion(self,)->DataIngestionArtifact:
        try:
            dataFrame = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataFrame)
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=self.data_ingestion_config.training_file_path,test_file_path=self.data_ingestion_config.testing_file_path)
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException
        


    
