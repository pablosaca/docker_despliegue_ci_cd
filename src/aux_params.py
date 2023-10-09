import os
import joblib
import pandas as pd
import tensorflow as tf
from lime.lime_text import LimeTextExplainer
from shiny import ui
from src.utils import Constants, clean_text, prep_neural_network

__all__ = ["user_input_select",
           "output_model"]


def user_input_select():
    return ui.panel_sidebar(ui.input_text_area("text", "Text area", placeholder="Enter text"),
                            ui.input_action_button("btn", "INCOME?", class_="btn-success")
                            )


def output_model(df: pd.DataFrame, name_path: str):

    # input text as dataframe (se limpia el texto)
    df['text'] = df['text'].apply(clean_text)

    dict_path = os.path.join(name_path, Constants.PREP_PATH.value)
    prep_dict = prep_neural_network(path=dict_path)  # text preprocessing token

    model_path = os.path.join(name_path, Constants.MODEL_PATH.value)
    model = joblib.load(model_path)  # tensorflow/keras model

    tokenizer_path = os.path.join(name_path, Constants.TOKENIZER_PATH.value)
    tokenizer = joblib.load(tokenizer_path)  # tensorflow/keras tokenizer preprocessing

    def model_predict(texts):
        _seq = tokenizer.texts_to_sequences(texts)
        _text_data = tf.keras.preprocessing.sequence.pad_sequences(_seq,
                                                                   maxlen=prep_dict["maxlen"],
                                                                   padding=prep_dict["padding"])
        return model.predict(_text_data)

    class_name_list = Constants.class_name.value
    explainer = LimeTextExplainer(class_names=class_name_list)

    exp_output = explainer.explain_instance(df['text'].values[0],
                                            model_predict,
                                            num_features=len(class_name_list),
                                            top_labels=len(class_name_list))

    # get probabilities given by neural model
    probs_df = pd.DataFrame(exp_output.predict_proba, columns=["Probs"], index=class_name_list)
    probs_df = probs_df.assign(Labels=probs_df.index)
    probs_df = probs_df.reset_index(drop=True).sort_values(by="Probs", ascending=False)

    # get tokens more important to make decision
    focus_tokens_df = pd.DataFrame(exp_output.as_list(), columns=["Tokens", "Value"])

    print("probabilities")
    print(probs_df)

    print("")
    print("tokens used")
    print(focus_tokens_df)

    return probs_df, focus_tokens_df
