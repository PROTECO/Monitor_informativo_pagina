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
    page_title="Configuracion",
    page_icon="💻",
)

st.write("# Eliminar imagen")


objetos = []
for my_bucket_object in my_bucket.objects.all():
    if ".Trash-1000/" in my_bucket_object.key or "anunciosTexto.js" in my_bucket_object.key:
        continue
    else:
        # st.write(my_bucket_object.key)
        objetos.append(my_bucket_object.key)
        
objeto = st.selectbox(
    "Que video deseas eliminar ",
    objetos,
)
descargas = os.listdir(".")
print()
if objeto not in descargas:
    os.system("rm *.jpg")
    with open(objeto, 'wb') as f:
        s3.download_fileobj('comercosing', objeto, f)
        f.seek(0)
    st.image(objeto)
else:
    st.image(objeto)
eliminar = st.checkbox('Eliminar')

if eliminar:
    st.write('Estas seguro que lo quieres eliminar')
    if st.button('si'):
        s3.delete_object(Bucket='comercosing',Key= objeto)
        st.write('imagen eliminado')
        st.balloons()


