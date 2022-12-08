## 1: CONFIGURACION DE ENTORNO
1- Crear un entorno virtual donde instalar paquetes de python

`py -m venv myenv`

2- Activar entorno virtual, en Windows, primero ejecutar en PowerShell, para permitir ejecutar script en la terminal de Visual Studio,  cualquier otro editor de texto o terminal

`Set-ExecutionPolicy RemoteSigned`

Si a todos, colocar Y y enter

3- Ya en la terminal ejecutar, se debe activar entorno virtual con el siguiente comando:

`\myenv\Scripts\activate`

4- Ya iniciado el entorno, instalar Django en entorno virtual:

`pip install django`

5- Iniciar un nuevo proyecto en el directorio, ejecutar lo siguiente :

`django-admin startproject portfolio .`

6- Verificar si hasta ahora, todo esta bien, ejecutando:

 `python manage.py runserver`

7- Crear aplicacion en el proyecto, ejecutando:

`python manage.py startapp jhonn`

8- Agregar la aplicacion creada en INSTALLED_APPS, esto se realiza en el archivo settings.py del proyecto principal, es decir, portafolio, se agrega al final, se vera algo asi:
```python
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'jhonn',
]
```