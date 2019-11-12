# Sistema de recomendación
Requisitos del sistema:
1. Tener instalado  python3 o anaconda,(https://www.aprendemachinelearning.com/instalar-ambiente-de-desarrollo-python-anaconda-para-aprendizaje-automatico/)
2. Tener instalada la bilblioteca ScikitLearn.
3. Tener instala la biblioteca Numpy
4. Tener instalado pandas.



Primero se deberá crear un entorno virtual en la carpeta sistema-de-recomendacon, esto se hará de la siguiente manera:

sistema-de-recomendacion$ python3 -m venv .env

Una vez hecho esto se tendrá que activar el entorno virtual creado, esto lo haremos de la siguiente manera:

sistema-de-recomendacion$ source /bin/.env/activate 

Sabremos que el sistema de recomendacion esta iniciado cuando aparezca un punto antes de la dirección de la carpeta.

(.)sitema-de-recomendacion$

Teniendo esto tenenmos que verificar que las bilbiotecas comentadas esten instaladas esto mediante el siguiente comando:
(.)sitema-de-recomendacion$ pip freeze

El cual mostraría algo como lo siguiente

Django==2.2.6
numpy==1.17.3
pandas==0.25.2
scikit-learn==0.21.3
    
    
Una vez hecho lo anterior se deberá acceder a la carpeta "sistema-de-recomendacion-django", posteriormente se tendrá que correr el servidor esto se hara de la siguiente forma:

(.)sistema-de-recomendacion-django$ python3 manage.py runserver

Ya corriendo el servidor se tendrá que acceder a la siguiente URL:

http://localhost:8000/eleccion

Al ingresar a la url es posible que tarde en cargar la pagína pues el algoritmo de recomendaciones tarda, si llega a pasar esto por favor recarguen la pagína.
