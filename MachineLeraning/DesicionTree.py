from sklearn.datasets import load_iris

from sklearn.tree import DecisionTreeClassifier

#Importar pandas 
import pandas as pd
import numpy as np

iris = load_iris()

df = pd.DataFrame(iris.data,
                  columns=['Sepal length (cm)', 'Sepal width (cm)', 'Petal length (cm)', 'Petal width (cm)'])

print(df.head(5))

x = iris.data[:, 2:]
y = iris.target

iris_df_sliced = df.iloc[:, 2:]
datos_entrenamiento =pd.DataFrame(
    data = np.column_stack([iris_df_sliced, y]),
    columns=['Petal length (cm)', 'Petal width (cm)', 'Result']
)
print(datos_entrenamiento)

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(x, y)