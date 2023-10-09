import re
import json
from enum import Enum


__all__ = ["Constants", "clean_text", "prep_neural_network"]


class Constants(Enum):

    # se crea una lista con los posibles outputs
    class_name = ["CriptoInfo", "DeportesCuatro", "Nutricion", "SensaCine", "Visita_Madrid"]

    # model and text preprocessing paths
    MODEL_PATH = 'nn_model.joblib'
    TOKENIZER_PATH = 'tokenizer.joblib'
    PREP_PATH = 'prep_text.json'


def clean_text(x: str) -> str:

    x = re.compile('\r').sub(' ', x)
    x = re.compile('\n').sub(' ', x)
    x = re.compile('"').sub('', x)
    x = re.compile('[+-]').sub('', x)
    x = re.compile(r'<[\w_]+').sub('', x)
    x = re.compile(r'>').sub(' ', x)
    # x = re.compile(r'@[\w_]+').sub('', x) #elimina menciones
    x = re.compile(r'https?://[\w_./]+').sub('', x)  # elimina URL
    # x = re.compile(r'#[\w_]+').sub('', x) #elimina hashtags
    return x


def prep_neural_network(path: str) -> dict:

    with open(path) as json_file:
        input_prep_text = json.load(json_file)

    return input_prep_text
