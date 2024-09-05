import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


with open("./customer_message_priority_classifier_model.pickle", "rb") as bin_file:
    _model = pickle.load(bin_file)


with open("./ttdif_vectorizer_bin.pickle", "rb") as bin_file:
    _vectorizer = pickle.load(bin_file)



def priority_pred(*args: str) -> list:
    texts: list = []
    for info in args:
        texts.append(info)
    transformer = _vectorizer.transform(texts)
    prediction = _model.predict(transformer)
    return list(prediction)

