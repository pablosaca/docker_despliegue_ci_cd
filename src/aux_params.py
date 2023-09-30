import joblib
import pandas as pd
from shiny import ui
from _utils import *


__all__ = ["user_input_select",
           "output_model"]


def user_input_select():
    return ui.panel_sidebar(ui.input_slider("age", "AGE", min=age["min"], max=age["max"], value=age["value"]),
                            ui.input_select("workclass", "WORKCLASS", workclass),
                            ui.input_select("education", "EDUCATION", education),
                            ui.input_radio_buttons("marital_status", "MARITAL STATUS", marital_status),
                            ui.input_select("occupation", "OCCUPATION", occupation),
                            ui.input_select("relationship", "RELATIONSHIP", relationship),
                            ui.input_radio_buttons("race", "RACE", race),
                            ui.input_select("gender", "GENDER", gender),
                            ui.input_numeric("capital_gain", "CAPTITAL GAIN",
                                             cap_gain["value"], min=cap_gain["min"], max=cap_gain["max"]),
                            ui.input_numeric("capital_loss", "CAPTITAL LOSS",
                                             cap_loss["value"], min=cap_loss["min"], max=cap_loss["max"]),
                            ui.input_numeric("hours_week", "HOURS PER WEEK",
                                             hp_week["value"], min=hp_week["min"], max=hp_week["max"]),
                            ui.input_select("native_country", "NATIVE_COUNTRY", native_country),
                            ui.input_action_button("btn", "INCOME?", class_="btn-success")
                            )


def output_model(df: pd.DataFrame, path: str):

    model = joblib.load(f"{path}")
    normalizer = joblib.load(path)

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

    # getting prediction
    # redes convolucionales - se añade una dimensión a los datos
    X = X.reshape(X.shape[0], X.shape[1], 1)
    prediction_proba = model.predict(X)

    output1 = round(prediction_proba[0][0] * 100, 2)
    pred = f"{str(output1)} %"
    return pred