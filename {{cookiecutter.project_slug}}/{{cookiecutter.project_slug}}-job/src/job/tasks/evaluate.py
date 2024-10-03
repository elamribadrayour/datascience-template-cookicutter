"""{{cookiecutter.project_name}} model testing with evaluation metrics"""

import numpy
import logging
from typing import Literal

import pandas
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import helpers.paths
import helpers.logger


def get_test_data(cache_path: str) -> pandas.DataFrame:
    """Load test data from a specified cache path."""
    path = helpers.paths.get_test_data_path(cache_path=cache_path)
    logging.info(f"Loading testing data from {path}")
    return pandas.read_parquet(path=path)


def get_train_data(cache_path: str) -> pandas.DataFrame:
    """Load test data from a specified cache path."""
    path = helpers.paths.get_train_data_path(cache_path=cache_path)
    logging.info(f"Loading train data from {path}")
    return pandas.read_parquet(path=path)


def get_metrics(y_true: numpy.ndarray, y_pred: numpy.ndarray):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    logging.info(f"Accuracy: {accuracy:.2f}")
    logging.info(f"Precision: {precision:.2f}")
    logging.info(f"Recall: {recall:.2f}")
    logging.info(f"F1 Score: {f1:.2f}")


def run_linear_regression(cache_path: str) -> None:
    """Run linear regression testing for {{cookiecutter.project_name}} with evaluation metrics."""
    helpers.logger.init()
    logging.info("Running model testing for {{cookiecutter.project_name}}")
    raise NotImplementedError


def run_xgboost_classifier(cache_path: str) -> None:
    """Run linear regression testing for {{cookiecutter.project_name}} with evaluation metrics."""
    helpers.logger.init()
    raise NotImplementedError


def run(
    cache_path: str, model: Literal["linear_regression", "xgboost_classifier"]
) -> None:
    if model == "linear_regression":
        return run_linear_regression(cache_path=cache_path)
    if model == "xgboost_classifier":
        return run_xgboost_classifier(cache_path=cache_path)
    raise ValueError("model has an unknown value")
