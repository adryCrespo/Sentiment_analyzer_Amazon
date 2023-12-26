import pandas as pd

def print_df(df):
    
    numero_filas, numero_columns = df.shape
    numero_missings = df.isna().sum().sum()
    numero_columnas_missings = len(df.isna().sum().loc[lambda x: x>0])
    
    print(f"Numero filas: {numero_filas}")
    print(f"Numero columnas: {numero_columns}")
    print(f"Numero columnas: {numero_missings}")
    print(f"Numero columnas con missings: {numero_columnas_missings}")

def load_dataset_train(raiz='C:/Proyectos/X01_sentiment_analyzer', nombre_fichero_trabajo='trabajo.csv'):

    ruta_completa = raiz + '/02_Datos/03_Trabajo/' + nombre_fichero_trabajo
    datos = pd.read_csv(ruta_completa,index_col=0, encoding='unicode_escape')
    return datos

def load_dataset_val(raiz='C:/Proyectos/X01_sentiment_analyzer', nombre_fichero_trabajo='validacion.csv'):

    ruta_completa = raiz + '/02_Datos/02_Validacion/' + nombre_fichero_trabajo
    datos = pd.read_csv(ruta_completa,index_col=0, encoding='unicode_escape')
    return datos