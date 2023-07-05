from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation

class TrainPipeline:
    def __init__(self) -> None:
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            logging.info('Starting data ingestion')
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f'ending data ingestion completed and {data_ingestion_artifact}')
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        

        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:

            logging.info('starting data validation')
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info('ending data validation')
            return data_validation_artifact
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



