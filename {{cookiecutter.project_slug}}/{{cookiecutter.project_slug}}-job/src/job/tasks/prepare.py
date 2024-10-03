"""prepare data for {{cookiecutter.project_name}}."""

import os
import logging

import pandas
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

import helpers.paths
import helpers.logger


def get_raw_data(cache_path: str) -> pandas.DataFrame:
    raise NotImplementedError


def set_train_test_data(data: pandas.DataFrame, cache_path: str) -> None:
    train_path = os.path.join(
        helpers.paths.get_data_path(cache_path=cache_path),
        "train.parquet",
    )
    test_path = os.path.join(
        helpers.paths.get_data_path(cache_path=cache_path),
        "test.parquet",
    )

    df_train, df_test = train_test_split(data)

    x_train = df_train.drop("Class", axis=1)
    y_train = df_train["Class"]

    smote = SMOTE(random_state=42)
    x_train_sm, y_train_sm = smote.fit_resample(x_train, y_train)
    df_train = pandas.concat(objs=[x_train_sm, y_train_sm], axis=1)
    logging.info("applied SMOTE for balancing the dataset")

    df_test.to_parquet(path=test_path, compression="gzip", engine="pyarrow")
    df_train.to_parquet(path=train_path, compression="gzip", engine="pyarrow")
    return


def run(cache_path: str) -> None:
    helpers.logger.init()
    logging.info("running data preparation for {{cookiecutter.project_name}}")
    data = get_raw_data(cache_path=cache_path)
    set_train_test_data(data=data, cache_path=cache_path)
