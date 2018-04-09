#!/bin/python3
import django_orm
from db.models import *

django_orm.migrate()

try:
    alice = User.objects.get(name='Alice')
except:
    alice = User.objects.create(name='Alice')

for i in User.objects.all():
    print("ID: " + str(i.id) + "\tUsername: " + i.name)
