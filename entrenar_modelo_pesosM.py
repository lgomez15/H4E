import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Paso 1: Cargar los datos
data = pd.read_csv('datos.csv')

# Paso 2: Definir las columnas de listas y categóricas
list_columns = ['Asignatura1', 'Asignatura2', 'Asignatura3', 'Asignatura4',
                'Asignatura5', 'Asignatura6', 'Asignatura7', 'Asignatura8',
                'Asignatura9', 'Asignatura10', 'Asignatura11', 'Asignatura12']

categorical_cols = ['sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

# Paso 3: Preprocesar los datos
def parse_list_column(column):
    return column.apply(lambda x: list(map(int, x.strip('[]').split(','))))

def preprocesar_datos(data, scaling_factor=0.5):
    # Procesar las columnas de listas
    for col in list_columns:
        data[col] = parse_list_column(data[col])

    # Calcular estadísticas para cada asignatura
    for col in list_columns:
        data[f'{col}_mean'] = data[col].apply(np.mean)
        data[f'{col}_std'] = data[col].apply(np.std)
        data[f'{col}_max'] = data[col].apply(np.max)
        data[f'{col}_min'] = data[col].apply(np.min)
    # Eliminar las columnas originales de listas
    data.drop(columns=list_columns, inplace=True)

    # Aplicar factor de escala a las características de las calificaciones
    grade_features = [f'{col}_{stat}' for col in list_columns for stat in ['mean', 'std', 'max', 'min']]
    data[grade_features] = data[grade_features] * scaling_factor

    # Aplicar One-Hot Encoding a las variables categóricas
    data = pd.get_dummies(data, columns=categorical_cols)

    # Asegurar que no haya valores faltantes
    data.fillna(0, inplace=True)

    return data

# Aplicar el preprocesamiento con un factor de escala para las calificaciones
scaling_factor = 1  # Ajusta este valor según lo que desees
data = preprocesar_datos(data, scaling_factor=scaling_factor)

# Paso 4: Separar características y variable objetivo
X = data.drop('G3', axis=1)
y = data['G3']

# Paso 5: Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 6: Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Paso 7: Evaluar el modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Error cuadrático medio (MSE): {mse}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse}')

# Paso 8: Guardar el modelo y las columnas de X_train
joblib.dump(model, 'modelo_entrenado_ajustado.pkl')
joblib.dump(X_train.columns, 'X_train_columns_ajustado.pkl')
