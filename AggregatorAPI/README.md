## INSTALL PACKAGES
pip install django \
pip install mysqlclient \
pip install djangorestframework 

## CONFIG DATABASE
### Install MySQL database
### Add Database(run sql query in SQLyog or Navicat)
CREATE DATABASE `Aggregate`CHARACTER SET utf8 COLLATE utf8_general_ci; \
USER: 'root' \
PASSWORD: '' \
PORT: 3306 
### Migrate database
python manage.py migrate 
### Create super user
python manage.py createsuperuser 

## RUN SERVER
python manage.py runserver 

