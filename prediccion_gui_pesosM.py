import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import joblib

# Paso 1: Cargar el modelo entrenado
model = joblib.load('modelo_entrenado_ajustado.pkl')

# Cargar las columnas de X_train para alinear las características
X_train_columns = joblib.load('X_train_columns_ajustado.pkl')

# Definir las columnas de listas y categóricas
list_columns = ['Asignatura1', 'Asignatura2', 'Asignatura3', 'Asignatura4',
                'Asignatura5', 'Asignatura6', 'Asignatura7', 'Asignatura8',
                'Asignatura9', 'Asignatura10', 'Asignatura11', 'Asignatura12']

categorical_cols = ['sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                    'reason', 'guardian', 'schoolsup', 'famsup', 'paid',
                    'activities', 'nursery', 'higher', 'internet', 'romantic']

# Definir las columnas numéricas
numeric_cols = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']

# Paso 2: Función para preprocesar los datos del usuario
def preprocesar_datos(data, scaling_factor=0.5):
    # Procesar las columnas de listas
    for col in list_columns:
        # Las listas ya están en formato de listas
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
    data = data.reindex(columns=X_train_columns, fill_value=0)

    return data

# Paso 3: Crear la interfaz gráfica
class App:
    def __init__(self, master):
        self.master = master
        master.title("Predicción de G3")

        self.entries = {}

        # Crear campos para variables categóricas con opciones predefinidas
        categorical_options = {
            'sex': ['M', 'F'],
            'address': ['U', 'R'],
            'famsize': ['LE3', 'GT3'],
            'Pstatus': ['A', 'T'],
            'Mjob': ['at_home', 'health', 'services', 'teacher', 'other'],
            'Fjob': ['at_home', 'health', 'services', 'teacher', 'other'],
            'reason': ['home', 'reputation', 'course', 'other'],
            'guardian': ['mother', 'father', 'other'],
            'schoolsup': ['yes', 'no'],
            'famsup': ['yes', 'no'],
            'paid': ['yes', 'no'],
            'activities': ['yes', 'no'],
            'nursery': ['yes', 'no'],
            'higher': ['yes', 'no'],
            'internet': ['yes', 'no'],
            'romantic': ['yes', 'no']
        }

        row_idx = 0
        for col in categorical_cols:
            label = tk.Label(master, text=f"{col}:")
            label.grid(row=row_idx, column=0, sticky='e')
            variable = tk.StringVar(master)
            variable.set(categorical_options[col][0])  # Valor por defecto
            option_menu = tk.OptionMenu(master, variable, *categorical_options[col])
            option_menu.grid(row=row_idx, column=1)
            self.entries[col] = variable
            row_idx += 1

        # Crear campos para variables numéricas
        for col in numeric_cols:
            label = tk.Label(master, text=f"{col}:")
            label.grid(row=row_idx, column=0, sticky='e')
            entry = tk.Entry(master)
            entry.grid(row=row_idx, column=1)
            self.entries[col] = entry
            row_idx += 1

        # Crear campos para las columnas de listas
        for col in list_columns:
            label = tk.Label(master, text=f"{col}:")
            label.grid(row=row_idx, column=0, sticky='e')
            entry = tk.Entry(master)
            entry.grid(row=row_idx, column=1)
            self.entries[col] = entry
            hint = tk.Label(master, text="(Valores separados por comas)")
            hint.grid(row=row_idx, column=2, sticky='w')
            row_idx += 1

        # Botón para realizar la predicción
        predict_button = tk.Button(master, text="Predecir G3", command=self.predecir)
        predict_button.grid(row=row_idx, column=0, columnspan=2)

    def predecir(self):
        # Obtener los datos ingresados
        data_input = {}
        try:
            # Variables categóricas
            for col in categorical_cols:
                valor = self.entries[col].get()
                data_input[col] = valor.strip()

            # Variables numéricas
            for col in numeric_cols:
                valor = self.entries[col].get()
                if valor == '':
                    messagebox.showerror("Error", f"Por favor, ingresa un valor para {col}.")
                    return
                data_input[col] = float(valor)

            # Columnas de listas
            for col in list_columns:
                valor = self.entries[col].get()
                if valor == '':
                    messagebox.showerror("Error", f"Por favor, ingresa los valores para {col}.")
                    return
                lista = [int(x.strip()) for x in valor.split(',')]
                data_input[col] = lista

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
            return

        # Convertir el diccionario en un DataFrame
        data_df = pd.DataFrame([data_input])

        # Preprocesar los datos
        scaling_factor = 1  # Debe ser el mismo que usaste en el entrenamiento
        data_preprocessed = preprocesar_datos(data_df, scaling_factor=scaling_factor)

        # Hacer la predicción
        prediccion = model.predict(data_preprocessed)

        # Mostrar el resultado
        messagebox.showinfo("Predicción", f"El valor predicho de G3 es: {prediccion[0]}")

# Ejecutar la aplicación
root = tk.Tk()
app = App(root)
root.mainloop()
