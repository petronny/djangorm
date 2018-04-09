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
# db/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, default="")
```

* Configure database
```python
# django_orm.py
database = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(module_name, 'db.sqlite3')
}
```

* Write your python code
```python
# demo.py
import django_orm
from db.models import *

django_orm.migrate()

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
* If you get errors when doing migrations, try removing `db/migrations`.

Acknownledgement
----
* [Official Django documentation about Django Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
* [dancaron/Django-ORM](https://github.com/dancaron/Django-ORM)
