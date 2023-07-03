from sensor.exception import SensorException
from sensor.logger import logging
import os, sys
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline


if __name__ =='__main__':
    training_pipeline =TrainPipeline()
    training_pipeline.run_pipeline()

