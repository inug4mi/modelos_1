import argparse
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from loguru import logger
import os

# Argument parser setup
parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='CSV file with training data')
parser.add_argument('--model_file', required=True, type=str, help='File to save the trained model')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='Overwrite the model file if it exists')

args = parser.parse_args()

data_file = args.data_file
model_file = args.model_file
overwrite = args.overwrite_model

# Check if the model file exists
if os.path.isfile(model_file):
    if overwrite:
        logger.info(f"Overwriting existing model file {model_file}")
    else:
        logger.info(f"Model file {model_file} already exists. Use --overwrite_model option to overwrite.")
        exit(-1)

logger.info("Loading training data")
df_train = pd.read_csv(data_file)

# Features and target variable
y = df_train["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(df_train[features])

# Training the model
logger.info("Fitting the model")
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)

# Saving the model
logger.info(f"Saving the model to {model_file}")
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

logger.info("Training completed successfully")
