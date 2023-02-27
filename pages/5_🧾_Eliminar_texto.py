import streamlit as st
import boto3
import os


ACCESS_KEY = "AKIA45UK4O2DWLU4XPMS"
SECRET_KEY = "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"

session = boto3.Session( aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

my_bucket = s3.Bucket('comercosing')

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)



st.set_page_config(
    page_title="Eliminar Texto",
    page_icon="🧾",
)

st.write("# Eliminar Texto")

bandera = False
for my_bucket_object in my_bucket.objects.all():
    if "anunciosTexto.js" in my_bucket_object.key:
        os.system("rm *.js")
        objeto = "anunciosTexto.js"
        with open(objeto, 'wb') as f:
            s3.download_fileobj('comercosing', objeto, f)

        # s3.download_fileobj('comercosing', ,"anunciosTexto.js")
        bandera = True
        

if bandera:
    archivo = open("anunciosTexto.js","r")
    contenido = []
    subir = []
    for linea in archivo:
        subir.append(linea)
        contenido.append(linea.replace(",","").replace(".","").replace("]","").replace("[","").replace("\n","").replace(";","").replace("'","").replace('"',""))
    print(contenido)
    archivo.close()
    
objeto = st.selectbox(
    "Que mensaje deseas eliminar ",
    contenido[1:-1],
)
st.write('Texto a Borrar:', objeto)
if st.button('Borrar'):
    archivo = open("anunciosTexto.js","w")
    subir.pop(contenido.index(objeto))
    archivo.writelines(subir)
    archivo.close()
    s3.upload_file("./anunciosTexto.js", 'comercosing', "anunciosTexto.js")
    st.balloons()
    st.write("# Actualizado por favor recarga la pagina si quieres eliminar otro texto")



