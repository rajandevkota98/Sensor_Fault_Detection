from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import ModelTrainerArtifact,ModelEvalutionArtifact,DataValidationArtifact
from sensor.entity.config_entity import ModelEvalutionConfig
import os,sys
import pandas as pd

from sensor.ml.metrics.classification_metric import get_classification_score
from sensor.ml.model.estimator import SensorModel
from sensor.utils.main_utils import save_object,load_object,write_yaml_file
from sensor.ml.model.estimator import ModelResolver

class ModelEvaluation:
    def __init__(self, model_eval_config:MemoryError,
                 data_validation_artifact:DataValidationArtifact,
                 model_trainer_artifact:ModelTrainerArtifact
                 ) -> ModelEvalutionArtifact:
        try:
            self.model_eval_config=model_eval_config
            self.data_validation_artifact=data_validation_artifact
            self.model_trainer_artifact=model_trainer_artifact
        except Exception as e:
            raise SensorException(e,sys)

    def initiate_model_evaluation(self,):
        try:
            logging.info('reading valid train file path and test file path')
            valid_train_file_path =self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            logging.info('coverting into dataframe')
            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)
            
            model_resolver = ModelResolver()
            model_file_path = self.model_trainer_artifact.trained_model_file_path
            model = load_object(file_path=model_file_path)

            is_model_accepted = True

            if model_resolver.is_model_exist():
                model_evaluation_artifact = ModelEvalutionArtifact(is_model_accepted=is_model_accepted,
                    changed_accuracy=None,
                    best_model_path=None,
                    trained_model_path=model_file_path,
                    train_model_metric_artifact=self.model_trainer_artifact.train_metric_artifact, 
                    best_model_metric_artifact=None)

           
            return model_evaluation_artifact

            
        except Exception as e:
            raise SensorException(e,sys)
        




