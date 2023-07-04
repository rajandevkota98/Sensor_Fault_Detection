from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    validationn_satus:bool
    valid_train_file_path:str
    invalid_train_file_path:str
    valid_test_file_path:str
    invalid_test_file_path:str
    data_drift_report_file_path:str