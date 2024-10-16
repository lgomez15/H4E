import pandas as pd
import numpy as np
import joblib

# Paso 1: Cargar el modelo entrenado
model = joblib.load('modelo_entrenado.pkl')

# Paso 2: Definir las columnas de listas y categóricas
list_columns = ['Asignatura1', 'Asignatura2', 'Asignatura3', 'Asignatura4',
                'Asignatura5', 'Asignatura6', 'Asignatura7', 'Asignatura8',
                'Asignatura9', 'Asignatura10', 'Asignatura11', 'Asignatura12']

categorical_cols = ['sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

# Paso 3: Cargar los datos de prueba
data_test = pd.read_csv('datos_prueba.csv')

# Paso 4: Preprocesar los datos de prueba
def parse_list_column(column):
    return column.apply(lambda x: list(map(int, x.strip('[]').split(','))))

def preprocesar_datos(data):
    # Convertir las columnas de listas en listas numéricas
    for col in list_columns:
        data[col] = parse_list_column(data[col])
    # Crear características estadísticas
    for col in list_columns:
        data[f'{col}_mean'] = data[col].apply(np.mean)
        data[f'{col}_std'] = data[col].apply(np.std)
        data[f'{col}_max'] = data[col].apply(np.max)
        data[f'{col}_min'] = data[col].apply(np.min)
    # Eliminar las columnas originales de listas
    data.drop(columns=list_columns, inplace=True)
    # Convertir variables categóricas usando One-Hot Encoding
    data = pd.get_dummies(data, columns=categorical_cols)
    return data

# Aplicar el preprocesamiento
data_test_processed = preprocesar_datos(data_test)

# Paso 5: Alinear las columnas con el modelo entrenado
# Cargar las columnas de X_train
X_train_columns = joblib.load('X_train_columns.pkl')

# Alinear las columnas
data_test_processed = data_test_processed.reindex(columns=X_train_columns, fill_value=0)

# Paso 6: Asegurar que no haya valores faltantes
data_test_processed.fillna(0, inplace=True)

# Paso 7: Hacer predicciones
predicciones = model.predict(data_test_processed)

# Paso 8: Mostrar las predicciones
print('Predicciones de G3 para los datos de prueba:')
for idx, pred in enumerate(predicciones):
    print(f'Registro {idx+1}: G3 predicho = {pred}')

# Paso 9: Comparar con los valores reales de G3 (si los tienes)
# Si tienes los valores reales de G3, puedes descomentar las siguientes líneas
# y añadir la columna 'G3' en 'datos_prueba.csv'

# real_G3 = data_test['G3'].values
# print('\nComparación de predicciones con valores reales:')
# for idx, (pred, real) in enumerate(zip(predicciones, real_G3)):
#     print(f'Registro {idx+1}: G3 real = {real}, G3 predicho = {pred}')

# # Calcular MSE y RMSE
# from sklearn.metrics import mean_squared_error
# mse = mean_squared_error(real_G3, predicciones)
# rmse = np.sqrt(mse)
# print(f'\nError cuadrático medio (MSE) en datos de prueba: {mse}')
# print(f'Raíz del error cuadrático medio (RMSE) en datos de prueba: {rmse}')
