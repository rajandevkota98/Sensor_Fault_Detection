from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys

class TrainPipeline:
    def __init__(self) -> None:
        self.training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

    def start_data_ingestion(self):
        try:
            logging.info('Starting data ingestion')
            logging.info('ending data ingestion')
            
        except Exception as e:
            raise SensorException(e,sys)
        
    def start_data_validation(self):
        try:
            logging.info('starting data validation')
            logging.info('ending data validation')
        except Exception as e:
            raise SensorException(e,sys)
            
    def start_data_transformation(self):
        try:
            logging.info('starting data transformation')
        except Exception as e:
            raise SensorException(e,sys)
            
    def start_model_trainer(self):
        try:
            logging.info('starting model trainer')
        except Exception as e:
            raise SensorException(e,sys)
            
    def start_model_evaluation(self):
        try:
            logging.info('starting model evalutaion')
        except Exception as e:
            raise SensorException(e,sys)


    def start_model_pusher(self):
        try:
            logging.info('starting model pusher')
        except Exception as e:
            raise SensorException(e,sys)
            
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)



