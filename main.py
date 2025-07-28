from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import sys


if __name__ == "__main__":
    try:
        # Initialize data ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Train data saved at: {train_data_path}")
        logging.info(f"Test data saved at: {test_data_path}")

        # Initialize data transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        logging.info("Data ingestion and transformation completed successfully.")
        model_trainer=ModelTrainer()
        r2_score=model_trainer.initiate_model_trainer(train_arr, test_arr)
        logging.info(f"Model training completed with R2 score: {r2_score}")
    except Exception as e:
        raise CustomException(e, sys)
