import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Paso 1: Cargar los datos
data = pd.read_csv('datos.csv')

# Paso 2: Preprocesar los datos
list_columns = ['Asignatura1', 'Asignatura2', 'Asignatura3', 'Asignatura4',
                'Asignatura5', 'Asignatura6', 'Asignatura7', 'Asignatura8',
                'Asignatura9', 'Asignatura10', 'Asignatura11', 'Asignatura12']

def parse_list_column(column):
    return column.apply(lambda x: list(map(int, x.strip('[]').split(','))))

for col in list_columns:
    data[col] = parse_list_column(data[col])

for col in list_columns:
    data[f'{col}_mean'] = data[col].apply(np.mean)
    data[f'{col}_std'] = data[col].apply(np.std)
    data[f'{col}_max'] = data[col].apply(np.max)
    data[f'{col}_min'] = data[col].apply(np.min)
data.drop(columns=list_columns, inplace=True)

categorical_cols = ['sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

data = pd.get_dummies(data, columns=categorical_cols)
data.fillna(0, inplace=True)

# Paso 3: Separar características y variable objetivo
X = data.drop('G3', axis=1)
y = data['G3']

# Paso 4: Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 5: Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Paso 6: Evaluar el modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Error cuadrático medio (MSE): {mse}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse}')

# Paso 7: Guardar el modelo
joblib.dump(model, 'modelo_entrenado.pkl')

# Función para preprocesar nuevos datos
def preprocesar_nuevos_datos(nuevos_datos):
    for col in list_columns:
        nuevos_datos[col] = parse_list_column(nuevos_datos[col])
    for col in list_columns:
        nuevos_datos[f'{col}_mean'] = nuevos_datos[col].apply(np.mean)
        nuevos_datos[f'{col}_std'] = nuevos_datos[col].apply(np.std)
        nuevos_datos[f'{col}_max'] = nuevos_datos[col].apply(np.max)
        nuevos_datos[f'{col}_min'] = nuevos_datos[col].apply(np.min)
    nuevos_datos.drop(columns=list_columns, inplace=True)
    nuevos_datos = pd.get_dummies(nuevos_datos, columns=categorical_cols)
    nuevos_datos = nuevos_datos.reindex(columns=X_train.columns, fill_value=0)
    return nuevos_datos

# Paso 8: Probar el modelo con nuevos datos (usaremos una muestra del conjunto de prueba)
sample = X_test.iloc[0]
real_value = y_test.iloc[0]
predicted_value = model.predict([sample])[0]


# Guardar las columnas de X_train, lo que hace x_train.columns es guardar las columnas de X_train en un archivo pkl
joblib.dump(X_train.columns, 'X_train_columns.pkl')


print(f'\nValor real de G3: {real_value}')
print(f'Predicción de G3: {predicted_value}')
