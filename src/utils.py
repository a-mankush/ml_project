import os
import sys

import dill
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj_path:
            dill.dump(obj, file_obj_path)

    except Exception as e:
        raise CustomException(e, sys) from e


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_true=y_train, y_pred=y_train_pred)
            test_model_score = r2_score(y_true=y_test, y_pred=y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys) from e


def load_object(file_path):
    try:
        with open(file_path, "rb") as f:
            return dill.load(f)
    except Exception as e:
        raise CustomException(e, sys) from e
