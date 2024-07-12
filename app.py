import streamlit as st
import re

def correct_line(line):
    if '0"0"0"' in line:
        parts = line.split('0"0"0"')
        if len(parts) > 1:
            second_part = parts[1]
            # Find the position of the fourth quote after the first part
            quote_indices = [m.start() for m in re.finditer('"', second_part)]
            if len(quote_indices) >= 4:
                corrected_second_part = second_part[quote_indices[3] + 1:]  # Start after the fourth quote
                corrected_line = parts[0] + '0"0"0"' + corrected_second_part
                return corrected_line
    return line

def process_file(uploaded_file):
    lines = uploaded_file.getvalue().decode("utf-8").splitlines()
    corrected_lines = []

    for line in lines:
        corrected_lines.append(correct_line(line))

    return "\n".join(corrected_lines)

st.title("Corrección de Archivo de Texto")

uploaded_file = st.file_uploader("Cargar archivo TXT", type="txt")

if uploaded_file is not None:
    corrected_content = process_file(uploaded_file)
    
    # Displaying a few corrected lines for verification
    st.text_area("Contenido corregido", corrected_content[:1000])
    
    st.download_button(
        label="Descargar archivo corregido",
        data=corrected_content,
        file_name="archivo_corregido.txt",
        mime="text/plain"
    )
