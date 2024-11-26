
import pandas as pd

def clean_csv(input_path, output_path):
    # Cargar los datos del archivo CSV
    data = pd.read_csv(input_path)
    
    # 1. Eliminar duplicados
    data.drop_duplicates(inplace=True)
    
    # 2. Manejar valores nulos
    data['Edad'].fillna(data['Edad'].median(), inplace=True)
    data['Genero'].fillna('No especificado', inplace=True)
    data['Saldo'].fillna(data['Saldo'].mean(), inplace=True)
    data['Activo'].fillna(0, inplace=True)
    data['Nivel_de_Satisfaccion'].fillna(data['Nivel_de_Satisfaccion'].mode()[0], inplace=True)
    
    # Guardar los datos limpios en un nuevo archivo CSV
    data.to_csv(output_path, index=False)
    print(f"Archivo limpio guardado en: {output_path}")

# Ejemplo de uso
if __name__ == "__main__":
    input_csv = "clientes_banco.csv"  # Ruta del archivo original
    output_csv = "clientes_banco_limpio.csv"  # Ruta del archivo limpio
    clean_csv(input_csv, output_csv)
