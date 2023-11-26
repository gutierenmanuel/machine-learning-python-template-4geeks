import os
import requests
from urllib.parse import urlparse


def descargar_archivo(url, carpeta_local='',nombre=None):
    try:

        # Obtener el nombre del archivo de la URL
        nombre_archivo = os.path.basename(urlparse(url).path)

        # Combinar la carpeta local y el nombre del archivo para obtener la ruta completa
        ruta_local = os.path.join(carpeta_local, nombre_archivo)

        # Verificar si el archivo ya existe
        if os.path.exists(ruta_local):
            print(f'El archivo {nombre_archivo} ya existe en la carpeta local.')
            ruta_local = os.path.join(carpeta_local, nombre)


        # Realizar la solicitud GET para descargar el archivo
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar si la solicitud fue exitosa

        # Guardar el contenido en el archivo local
        with open(ruta_local, 'wb') as archivo_local:
            archivo_local.write(respuesta.content)

        print(f'Archivo descargado exitosamente en: {ruta_local}')

    except requests.exceptions.RequestException as e:
        print(f'Error al descargar el archivo: {e}')


## ---


import pandas as pd
import dataframe_image as dfi

def dataframe_to_image(dataframe,ruta_imagen):

    dfi.export(dataframe,ruta_imagen)