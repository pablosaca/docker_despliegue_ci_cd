import os
import joblib

from enum import Enum

import pandas as pd


__all__ = ["Constants", "output_model"]


PATH = os.path.dirname(__file__)
PATH = PATH.replace(r"\src", "")
PATH = os.path.join(PATH, 'model')


class Constants(Enum):
    THRESHOLD = 0.3


def output_model(df: pd.DataFrame, path: str):

    # cargar path
    model = joblib.load(f'{path}/rf_calib_model.joblib')
    normalizer = joblib.load(f'{path}/normalization.joblib')

    # convert to dummy variables
    category_columns = list(df.select_dtypes(include=['category', 'object']).columns)
    other_columns = list(df.select_dtypes(exclude=['category', 'object']).columns)

    df_dummy = pd.get_dummies(df[category_columns], drop_first=False, dtype=float)

    df_num = df[other_columns]
    df = pd.concat([df_num, df_dummy], axis=1)
    del df_dummy, df_num

    # all columns - add other of dummy features
    train_columns = list(normalizer.feature_names_in_)
    add_col = [col for col in train_columns if col not in df.columns]

    for col in add_col:
        df[col] = 0  # se incluye con valor a cero

    df = df[train_columns]  # la muestra a predecir con el mismo orden que la muestra de entrenamiento

    # normalize variables
    X = normalizer.transform(df)

    # getting prediction: array [pos(0), pos(1)] -> [major, minor]
    minor_class_prob = list(model.predict_proba(X)[:, 1])
    return minor_class_prob
