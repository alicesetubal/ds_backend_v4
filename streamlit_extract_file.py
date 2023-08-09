import streamlit as st
import os
from extract_file import TextExtractor 


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


    



if check_password():
    st.header("Welcome to Extract File :smile:")
    arquivo = st.file_uploader('Insira seu arquivo:', type=['csv', 'xlsx', 'pdf', 'txt', 'docx'])
    
    if arquivo is not None:
        temp_folder= "temp"
        if not os.path.exists(temp_folder)
            os.makedirs(temp_folder)
            
        temp_filename = os.path.join(temp_folder, arquivo.name)
        
        with open(temp_filename, "wb") as f:
            f.write(arquivo.getbuffer())
        
        filename = os.path.join("temp", arquivo.name)
        
        if arquivo.type == 'text/csv':
            texto = TextExtractor.extract_text_from_csv(filename)
      
        elif arquivo.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            texto = TextExtractor.extract_text_from_xlsx(filename)
      
        elif arquivo.type == 'application/pdf':
            texto = TextExtractor.extract_text_from_pdf(filename)
            
        elif arquivo.type == 'text/plain':
            texto = TextExtractor.extract_text_from_file(filename, 'txt')
            
        elif arquivo.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            texto = TextExtractor.extract_text_from_file(filename, 'docx')
        
        else:
            st.error("Tipo de arquivo não suportado.")
            st.stop()
            
        st.header("O texto extraído foi:")
        st.code(texto)
        
        os.remove(temp_filename)