import pandas as pd
import numpy as np
import joblib

# Paso 1: Cargar el modelo entrenado
model = joblib.load('modelo_entrenado_ajustado.pkl')

# Definir las columnas de listas y categóricas
list_columns = ['Asignatura1', 'Asignatura2', 'Asignatura3', 'Asignatura4',
                'Asignatura5', 'Asignatura6', 'Asignatura7', 'Asignatura8',
                'Asignatura9', 'Asignatura10', 'Asignatura11', 'Asignatura12']

categorical_cols = ['sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

# Paso 2: Cargar los datos de prueba
data_test = pd.read_csv('datos_prueba.csv')

# Paso 3: Preprocesar los datos de prueba
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

    # Alinear las columnas con las del modelo entrenado
    X_train_columns = joblib.load('X_train_columns_ajustado.pkl')
    data = data.reindex(columns=X_train_columns, fill_value=0)

    # Asegurar que no haya valores faltantes
    data.fillna(0, inplace=True)

    return data

# Aplicar el preprocesamiento con el mismo factor de escala
scaling_factor = 0.3  # Debe ser el mismo que usaste en el entrenamiento
data_test_processed = preprocesar_datos(data_test, scaling_factor=scaling_factor)

# Paso 4: Hacer predicciones
predicciones = model.predict(data_test_processed)

# Paso 5: Mostrar las predicciones
print('Predicciones de G3 para los datos de prueba:')
for idx, pred in enumerate(predicciones):
    print(f'Registro {idx+1}: G3 predicho = {pred}')
