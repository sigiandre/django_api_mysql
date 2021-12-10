# django_api_mysql
REST API con Python, Django y MySQL (GET, POST, PUT, DELETE)

REST API con Python, Django y MySQL (GET, POST, PUT, DELETE)
https://www.youtube.com/watch?v=hL52_nB5QSw

### instalar python virtual
virtualenv -p python3 env

### para activarlo el comando python
.\env\Scripts\activate o activate

### instalar Django
pip install Django==3.2.4
python.exe -m pip install --upgrade pip

### ver las versiones instaladas
pip list

### crear una startproject proyecto con admin-django
django-admin startproject Proyecto_API

### crear otra con startapp
django-admin startapp api

### instalar mysql client
pip install mysqlclient pymysql

### ejecutar migracion
python manage.py makemigrations

### generar nuestras tablas
python manage.py migrate

### guardar nuestra dependencia de nuestro proyecto
pip freeze > requirements.txt

### crear un super usuario
python manage.py createsuperuser

### Ejecutar el proyecto
python manage.py runserver
