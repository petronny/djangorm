Simplest Django ORM
====
This is a Django ORM template that allows you to use Django's excellent ORM without having to use the rest of Django.

Dependencies
----
* Django

Installation
---
Just clone the repository to whatever you like.

Usage
----

* Setting up the default database (SQLite)
```python
# [your_module_name]/__init__.py
import os
from pathlib import Path
from djangorm import DjangORM

db = DjangORM(module_name=Path(__file__).parent.name)
db.configure()
db.migrate()
```

* Setting up a custom database (MySQL)
```python
# [your_module_name]/__init__.py
from djangorm import DjangORM

mysql_config = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': 'host',
    'NAME': 'name',
    'USER': 'user',
    'PASSWORD': 'password',
}
db = DjangORM(module_name=Path(__file__).parent.name, database=mysql_config)
db.configure()
db.migrate()
```

* Define the models:
```python
# [your_module_name]/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, default="")
```

* Write your python code
```python
from [your_module_name].models import *

try:
    alice = User.objects.get(name='Alice')
except User.DoesNotExist:
    alice = User(name='Alice')
    alice.save()

for user in User.objects.all():
    print("ID: %d\tUsername: %s" % (user.id, user.name))
```

Tips
----
* If you get errors when doing migrations, try removing `[your_module_name]/migrations`.

* There is a function that checking if all the fields are correct.
```python
db.check_models(models)
```

* Specify the relative path of the module
```python
db = DjangORM(module_name='[your_module_name]', module_path='[relative_path]')
```

Acknownledgement
----
* [Official Django documentation about Django Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
* [dancaron/Django-ORM](https://github.com/dancaron/Django-ORM)
