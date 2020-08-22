from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd


# All sklearn Transforms must have the `transform` and `fit` methods
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

class AddMediaNotasExatas(BaseEstimator, TransformerMixin):
  '''Recebe uma string para ser o nome da coluna de médias'''

  def __init__(self, nome_da_coluna):
    self.nome = nome_da_coluna

  def fit(self, X, y=None):
    return self

  def media_notas(self, x):
    notas = []
    notas.append(x['NOTA_MF'])
    notas.append(x['NOTA_GO'])

    media = np.mean(notas) 
    return pd.Series(data=[media], index=[self.nome])

  def transform(self, X):
    df2 = X.copy()

    coluna_media_exatas = df2.apply(self.media_notas, axis=1)
    df2 = df2.join(coluna_media_exatas)
    return df2

class AddNotasHumanas(BaseEstimator, TransformerMixin):
  '''Recebe uma string para ser o nome da coluna de médias'''

  def __init__(self, nome_da_coluna):
    self.nome = nome_da_coluna

  def fit(self, X, y=None):
    return self

  def media_notas(x):
    notas = []
    notas.append(x['NOTA_DE'])
    notas.append(x['NOTA_EM'])

    media = np.mean(notas) 

    return pd.Series(data=[media], index=[self.nome])

  def transform(self, X):
    df2 = X.copy()

    coluna_media_humanas = df2.apply(self.media_notas, axis=1)
    df2 = df2.join(coluna_media_humanas)
    return df2

All sklearn Transforms must have the `transform` and `fit` methods
class AddNotasGeral(BaseEstimator, TransformerMixin):
  '''Recebe uma string para ser o nome da coluna de médias'''

  def __init__(self, nome_da_coluna):
    self.nome = nome_da_coluna

  def fit(self, X, y=None):
    return self

  def media_notas(x):
    notas = []
    notas.append(x['NOTA_DE'])
    notas.append(x['NOTA_EM'])
    notas.append(x['NOTA_MF'])
    notas.append(x['NOTA_GO'])

    media = np.mean(notas) 

    return pd.Series(data=[media], index=[self.nome])

  def transform(self, X):
    df2 = X.copy()

    coluna_media_geral = df2.apply(self.media_notas, axis=1)
    df2 = df2.join(coluna_media_geral)
    return df2