"""{{cookiecutter.project_name}} model training"""

import logging
from typing import Literal

import pandas

import helpers.paths
import helpers.logger


def get_train_data(cache_path: str) -> pandas.DataFrame:
    path = helpers.paths.get_train_data_path(cache_path=cache_path)
    logging.info(f"loading training data from {path}")
    return pandas.read_parquet(path=path)


def run_xgboost_classifier(cache_path: str) -> None:
    helpers.logger.init()
    logging.info(
        "running xgboost classifier model training for {{cookiecutter.project_name}}"
    )
    raise NotImplementedError


def run_linear_regression(cache_path: str) -> None:
    helpers.logger.init()
    logging.info(
        "running xgboost classifier model training for {{cookiecutter.project_name}}"
    )
    raise NotImplementedError


def run(
    cache_path: str, model: Literal["linear_regression", "xgboost_classifier"]
) -> None:
    if model == "xgboost_classifier":
        return run_xgboost_classifier(cache_path=cache_path)
    if model == "linear_regression":
        return run_linear_regression(cache_path=cache_path)
    raise ValueError("model has an unknown value")
