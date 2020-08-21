from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

# All sklearn Transforms must have the `transform` and `fit` methods
class MediaNotas(BaseEstimator, TransformerMixin):
  '''Recebe uma string para ser o nome da coluna de médias'''

  def __init__(self, nome_da_coluna):
    self.nome = nome_da_coluna

  def fit(self, X, y=None):
    return self

  def media_notas(self, x):
    notas = []
    notas.append(x['NOTA_DE'])
    notas.append(x['NOTA_EM'])
    notas.append(x['NOTA_MF'])
    notas.append(x['NOTA_GO'])
    media = np.sum(notas)/4
    return pd.Series(data=[media], index=[self.nome])

  # Para transformar nunca vai o y
  def transform(self, X):
    data = X.copy()

    coluna_media = data.head().apply(self.media_notas, axis=1)
    data_com_media = data.join(coluna_media)
    return data_com_media