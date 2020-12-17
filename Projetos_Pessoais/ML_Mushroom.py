import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

dados = pd.read_csv('D:/mushrooms.csv')

dados['class'] = dados['class'].replace('p', 1)
dados['class'] = dados['class'].replace('e', 0)

x = dados['class']
y = dados.drop('class', axis=1)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

resultante = modelo.score(x_teste, y_teste)
print(f'Precisão: {resultante}')
