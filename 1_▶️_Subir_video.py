import streamlit as st
import os
import boto3
from PIL import Image

st.set_page_config(
    page_title="Configuracion",
    page_icon="💻",
)

ACCESS_KEY = "AKIA45UK4O2DWLU4XPMS"
SECRET_KEY = "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"

session = boto3.Session( aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

my_bucket = s3.Bucket('comercosing')

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
objetos = []
for my_bucket_object in my_bucket.objects.all():
    if ".Trash-1000/" in my_bucket_object.key or "anunciosTexto.js" in my_bucket_object.key:
        continue
    else:
        # st.write(my_bucket_object.key)
        objetos.append(my_bucket_object.key)
numbers = []
for archivos in objetos:
    numbers.append(max([int(letras)for letras in archivos.split(".") if letras.isdigit()]))
    
st.title("Subir imagen")

uploaded_files = st.file_uploader("Elige la imagen...", type=['jpg','png','jpeg'],accept_multiple_files=True)
temporary_location = False
os.system("rm *.jpg")
if uploaded_files is not None:
    bytes_data = []
    numeros = list(range(max(numbers)))
    faltantes = list(set(numeros) - set(numbers))
    print(faltantes)
    nombres = []
    valor = max(numbers)
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        image.thumbnail((1920, 1080))
        if len(faltantes) != 0:
            print(faltantes,faltantes is not None)
            bandera = faltantes.pop()
            print(bandera,faltantes)
            nombres.append(str(bandera) +'.jpg')
            image.save(str(bandera)+'.jpg')
        else:
            valor +=1
            nombres.append(str(valor)+'.jpg')
            image.save(str(valor)+'.jpg')
        bytes_data.append(image)
        st.image(image)  
        print(image)
        
    Subir = st.checkbox('Subir')
    if Subir:
        st.write('Estas seguro que deseas agregar la imagen')
        if st.button('si'):
            i = 0
            for uploaded_file in uploaded_files:
                s3.upload_file(nombres[i], 'comercosing', nombres[i])
                i += 1
                st.write('imagen subido')
                st.balloons()






