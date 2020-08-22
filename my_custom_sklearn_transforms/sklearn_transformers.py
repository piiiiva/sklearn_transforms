from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        df = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return df.drop(labels=self.columns, axis='columns')

class AddMedias(BaseEstimator, TransformerMixin):

  def __init__(self, name, columns):
    self.columns = columns
    self.name = name

  def fit(self, X, y=None):
    return self

  def media_notas(self, data):
    notas = []

    notas.append(data[self.columns])

    media = np.mean(notas) 

    return pd.Series(data=[media], index=[self.name])

  def transform(self, X):
    df = X.copy()

    coluna_media = df.apply(self.media_notas, axis=1)
    df = df.join(coluna_media)
    return df