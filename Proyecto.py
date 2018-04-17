
# coding: utf-8

# # INTELIGENCIA ARTIFICIAL
# 
# ## PROYECTO 6: Clasificador de Plantas.
# 
# ### Integrantes: 
# - Juan David Cardona Molina.
# - Natalia Isaza
# - Santiago Giraldo.
# 
# ### Breve Introducción:
# Este programa esta diseñado para el reconocimiento de plantas mediante captura de vídeo.
# 
# El entrenamiento usado se hizo mediante las herramientas por defecto del OpenCV.
# 
# Opencv_createsamples para el conjunto de imágenes positivas (Imágenes que contenan plantas), este programa creará un archivo de vector.
# 
# Opencv_traincascade el entrenamiento, usando el vector creado por el opencv_createsamples y el conjunto de imágenes negativas, dando como resultado, un archivo .xml de entrenamiento.
# 
# Una vez hecho lo anterior, se carga con el clasificador que trae la librería cv2 de Opencv para python.
# 
# ### Entrenamiento
# •	Descargar OpenCV para Windows 
# •	Crearemos una carpeta llamada Proyecto
# ![Sin titulo](2.png)
# 
# •	La idea es seguir esta estructura:
# -En data encontraremos nuestro vector y nuestro entrenamiento.xml
# -En Negativa encontraremos todas las imágenes que NO contengan plantas
# -En positivo encontraremos todas las imágenes que contengan plantas
# -Archivo negativas.txt contendrá el directorio y el nombre de la imagen seguido de la extensión
# -Archivo positivas.txt contendrá el directorio y el nombre de la imagen seguido de la extensión, además, las coordenadas.
# ![Sin titulo](3.png)
# 
# •	POSITIVA 
# ![Sin titulo](4.png)
# 
# •	NEGATIVA
# ![Sin titulo](5.png)
# 
# •	Con este programa obtendremos las coordenadas de las imágenes positivas de nuestro proyecto.
# ![Sin titulo](6.png)
# 
# •	En la carpeta rawdata colocaremos nuestras imágenes positivas en formato BMP.
# Una vez hecho los anterio, ejecutamos el programa objectmarker.exe y pasando el mause por la imagen,crearemos un cuadro, seleccionandoasi nuestra planta. Una vez seleccionada, presionamos la tecla ESPACIO Y ENTER para continuar con la sigueinte imagen.
# Al final nos creara un archivo info.txt con nuestras condenadas para casa imagen.
# 
# ![Sin titulo](7.png)
# ![Sin titulo](8.png)
# 
# •	Para que nuestro entrenamiento funcione y lo podamos cargar al programa todavía nos hace falta 2 archivos. Nuestro archivo de vector y, la hoja xml de entrenamiento…
# Para ello, ejecutaremos dos comandos en la consola de Windows (CMD) O bien, crear dos bat’s para cada proceso. Samples.bat generara nuestro archivo de vector con las imágenes positivas generadas y el archivo positivas.txt, traincascade.bat generara el entrenamiento  que  cargaremos al final a nuestro proyecto. Para ello, juntara positivas con negativas, tomando el vector y las imágenes negativas creadas.
# ![Sin titulo](9.png)
# ![Sin titulo](10.png)
# 
# ## Resultado
# ![Sin titulo](11.png)
# 
# ## Bibliografía
# 
# https://media.readthedocs.org/pdf/opencv-python-tutroals/latest/opencv-python-tutroals.pdf
# 
# https://www.docs.opencv.org/2.4.9/
# 
# 

# In[6]:


# LIBRERÍAS
import numpy as np # Importamos la librería numpy con alias np.
import cv2 as cv # Importamos la librería cv2 con alias cv.

# CUERPO DEL PROGRAMA
def cargar_entrenamiento():
    entrenamiento = cv.CascadeClassifier('entrenamiento_minimo.xml') # Cargamos el entrenamiento.
    return entrenamiento
    
def reconocimiento():    
    entrenamiento = cargar_entrenamiento() # Guardo lo que retorne la función entrenamiento.
    
    captura = cv.VideoCapture(0) # Inicializamos la captura de vídeo.
    # captura = cv.VideoCapture(0) - Para abrir Camara.

    while(True):
        ret, imagen = captura.read() # Leemos lo que hay en la variable captura y lo guardamos en dos variables.
        gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY) # Convertimos la imagen a blanco y negro.
        plantas = entrenamiento.detectMultiScale(gris, 1.3, 5) # Buscamos las coordenadas y guardamos su posición.

        for (posicion_x,posicion_y,ancho,largo) in plantas:
            cv.rectangle(imagen,(posicion_x,posicion_y),(posicion_x+ancho,posicion_y+largo),(125,255,0),2) # Crea un rectangulo en las coordenadas.

        cv.imshow('img',imagen) # Mostramos la imagen.

        if cv.waitKey(1) & 0xFF == ord('e'): # Con la tecla E cerramos el programa.
            break

    captura.release()
    cv.destroyAllWindows()

def main():
    reconocimiento() # Llamando la función del reconocimiento de plantas.


# In[7]:


if __name__ == '__main__':
    main()

