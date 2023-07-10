from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import ModelPusherArtifact,ModelEvalutionArtifact
from sensor.entity.config_entity import ModelPusherConfig
import os,sys

class ModelPusher:
    def __init__(self,model_evaluation_artifact:ModelEvalutionArtifact, model_pusher_config:ModelPusherConfig):
        try:
            self.model_evaluation_artifact=model_evaluation_artifact
            self.model_pusher_config=model_pusher_config
        except Exception as e:
            raise SensorException(e,sys)

