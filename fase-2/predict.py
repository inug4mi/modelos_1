import argparse
import pandas as pd
import pickle
from loguru import logger
import os

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, type=str, help='CSV file with input data')
parser.add_argument('--model_file', required=True, type=str, help='File with the trained model')
parser.add_argument('--predictions_file', required=True, type=str, help='File to save the predictions')

args = parser.parse_args()

input_file = args.input_file
model_file = args.model_file
predictions_file = args.predictions_file

# Check if the input file and model file exist
if not os.path.isfile(model_file):
    logger.error(f"Model file {model_file} does not exist")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"Input file {input_file} does not exist")
    exit(-1)

logger.info("Loading input data")
df_test = pd.read_csv(input_file)
features = ["Pclass", "Sex", "SibSp", "Parch"]
X_test = pd.get_dummies(df_test[features])

# Loading the model
logger.info("Loading the model")
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Making predictions
logger.info("Making predictions")
predictions = model.predict(X_test)

# Saving predictions to file
logger.info(f"Saving predictions to {predictions_file}")
output = pd.DataFrame({'PassengerId': df_test.PassengerId, 'Survived': predictions})
output.to_csv(predictions_file, index=False)

logger.info("Predictions completed successfully")
