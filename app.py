import streamlit as st
import re

def modificar_linea(linea):
    # Aplicar espacio y comillas entre "1" y "8000"
    linea = re.sub(r'("1")(\d+)', r'\1 "\2"', linea)
    
    # Quitar 0"0 y reemplazarlo por + después de 8000""
    linea = re.sub(r'8000""0"0"', '8000"+"', linea)
    
    # Borrar todo lo que se encuentra entre la " 11 y la 13
    linea = re.sub(r'" 11.*?13', '" 1113', linea)
    
    return linea

def procesar_archivo(contenido):
    lineas = contenido.split('\n')
    lineas_modificadas = [modificar_linea(linea) for linea in lineas if linea.strip()]
    return '\n'.join(lineas_modificadas)

st.title('Modificador de Registros')

archivo_subido = st.file_uploader("Sube tu archivo de texto", type="txt")

if archivo_subido is not None:
    contenido = archivo_subido.getvalue().decode("utf-8")
    contenido_modificado = procesar_archivo(contenido)
    
    st.text("Vista previa del contenido modificado:")
    st.text(contenido_modificado[:500] + "..." if len(contenido_modificado) > 500 else contenido_modificado)
    
    st.download_button(
        label="Descargar archivo modificado",
        data=contenido_modificado,
        file_name="archivo_modificado.txt",
        mime="text/plain"
    )
