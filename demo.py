#!/bin/python3
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
