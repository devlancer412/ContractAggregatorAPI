## INSTALL PACKAGES

```shell
pip install django
pip install mysqlclient
pip install djangorestframework
pip install web3
```

## CONFIG DATABASE

### Install MySQL database

### Add Database(run sql query in SQLyog or Navicat)

CREATE DATABASE `Aggregate`CHARACTER SET utf8 COLLATE utf8_general_ci; \
USER: 'root' \
PASSWORD: '' \
PORT: 3306

### Migrate database

```shell
python manage.py migrate
```

### Create super user

```shell
python manage.py createsuperuser
```

## RUN SERVER

```shell
python manage.py runserver
```
