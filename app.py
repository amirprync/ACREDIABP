import streamlit as st
import re
from io import StringIO

# Función para modificar los registros
def modify_record(record):
    # Aplicar el espacio y agregar la comilla entre "1" y "8000"
    record = re.sub(r'("1")("8000")', r'\1 "\2', record)
    # Eliminar el "0" "0" después de "8000"
    record = re.sub(r'("8000")"0""0"', r'\1', record)
    return record

# Configuración de la página
st.title("Modificación de Registros")
st.write("Sube un archivo TXT, se modificarán los registros según las especificaciones, y podrás descargar el archivo modificado.")

# Cargar archivo
uploaded_file = st.file_uploader("Sube el archivo TXT", type=["txt"])

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
        file_name="archivo_modificado.txt",
        mime="text/plain"
    )
import streamlit as st
import re
from io import StringIO

# Función para modificar los registros
def modify_record(record):
    # Aplicar el espacio y agregar la comilla entre "1" y "8000"
    record = re.sub(r'("1")("8000")', r'\1 "\2', record)
    # Eliminar el "0" "0" después de "8000"
    record = re.sub(r'("8000")"0" "0"', r'\1', record)
    return record

# Configuración de la página
st.title("Modificación de Registros")
st.write("Sube un archivo TXT, se modificarán los registros según las especificaciones, y podrás descargar el archivo modificado.")

# Cargar archivo
uploaded_file = st.file_uploader("Sube el archivo TXT", type=["txt"])

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
        file_name="archivo_modificado.txt",
        mime="text/plain"
    )
