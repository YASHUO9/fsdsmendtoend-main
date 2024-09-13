
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.model_trainer import ModelTrainer
from src.DimondPricePrediction.components.data_transformation import DataTransformation



object = DataIngestion()
train_data_path,test_data_path = object.initiate_data_ingestion()
data_transformation = DataTransformation()
train_arr,test_arr = data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer=ModelTrainer()
model_trainer.initate_model_training(train_arr,test_arr)


