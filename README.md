Simplest Django ORM
====
This is a Django ORM template that allows you to use Django's excellent ORM without having to use the rest of Django.

Dependencies
----
* Django

Usage
----

* Define the models:
```python
# [your_module_name]/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, default="")

```

* Using the default database (SQLite)
```python
from djangorm import DjangORM

db = DjangORM(module_name='[your_module_name]')
db.configure()
db.migrate()

```

* Using a custom database (MySQL)
```python
from djangorm import DjangORM

mysql_config = {
    'ENGINE': 'django.db.backends.mysql',
    'HOST': 'host',
    'NAME': 'name',
    'USER': 'user',
    'PASSWORD': 'password',
}
db = DjangORM(module_name='[your_module_name]', database=mysql_config)
db.configure()
db.migrate()

```

* Write your python code
```python
from djangorm import DjangORM
db = DjangORM(module_name='[your_module_name]')
db.configure()
db.migrate()
from test.models import *

try:
    alice = User.objects.get(name='Alice')
except:
    alice = User(name='Alice')
    alice.save()

for user in User.objects.all():
    print("ID: %d\tUsername: %s" % (user.id, user.name))

```

Tips
----
* If you get errors when doing migrations, try removing `[your_module_name]/migrations`.

Acknownledgement
----
* [Official Django documentation about Django Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
* [dancaron/Django-ORM](https://github.com/dancaron/Django-ORM)
