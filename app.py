import streamlit as st
import pandas as pd
import re
from io import StringIO

# Función para modificar los registros
def modify_record(record):
    # Primer cambio
    record = re.sub(r'("1")("8000")', r'\1 "\2', record)
    # Segundo cambio
    record = re.sub(r'("8000")("0" "0")', r'\1', record)
    return record

# Cargar archivo
uploaded_file = st.file_uploader("Sube el archivo CSV", type=["csv", "txt"])

if uploaded_file is not None:
    # Leer archivo
    string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
    data = string_data.read().splitlines()
    
    # Modificar cada registro
    modified_data = [modify_record(record) for record in data]
    
    # Convertir a un solo string
    result = "\n".join(modified_data)
    
    # Mostrar el resultado
    st.text_area("Archivo modificado", result, height=300)
    
    # Descargar el archivo modificado
    st.download_button(
        label="Descargar archivo modificado",
        data=result,
        file_name="archivo_modificado.csv",
        mime="text/csv"
    )

# Instrucciones para el usuario
st.write("""
    1. Sube el archivo CSV o TXT con los registros.
    2. El archivo será modificado automáticamente.
    3. Podrás descargar el archivo modificado.
""")
