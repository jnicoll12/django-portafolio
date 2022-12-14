## 1: CONFIGURACIÓN DE ENTORNO
1- Crear un entorno virtual donde instalar paquetes de python

`py -m venv myenv`

2- Activar entorno virtual, en Windows, primero ejecutar en PowerShell, para permitir ejecutar script en la terminal de Visual Studio,  cualquier otro editor de texto o terminal

`Set-ExecutionPolicy RemoteSigned`

Si, a todos, colocar Y y enter

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
## 2: CONFIGURACIÓN DE LA APLICACION

9- Creando modelos según nuestra plantilla de pagaina de portafolio (los archivos se encuentran en archivo models.py)

10- Una ves agregado nuestro modelo, se procede a realizar las migraciones.

Preparar el modelo con las últimas modificaciones:

`python manage.py makemigrations`

Hacer la migración a la bd:
`python manage.py migrate`

11- Crear un super usuario para administrar e ingresar en el panel de login

`python manage.py createsuperuser`

12- Se agregan los modelos en el archivo admin.py del archivo jhonn, para que se muestre en el admin y poder agregar informacion de manera grafica

13- Configurando la ruta y las URL de los archivos estáticos

```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
14- Importar en el archivo urls.py del proyecto principal en este caso, portafolio
```python
from django.conf import settings
from django.conf.urls.static import static
```
15- Indicarle a Django dónde encontrar los archivos estáticos mientras la aplicacion se ejecuta en el navegador, se realiza en el archivo urls.py del proyecto principal en este caso, portafolio, fuera de urlpatterns[]

```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
```
16- Agregar en el archivo views.py
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

17- Crear archivo URLS.py en la aplicacion del proyecto, es decir, en jhonn y agregar lo siguiente
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```
## 3: CONFIGURACIÓN DE APP CON REILWAY

18- Reilway, necesita el paque gunicorn, asi que lo instalamos con el siguiente comando:

`pip install gunicorn`

18- Crear, el archivo llamado Procfile en la raiz: