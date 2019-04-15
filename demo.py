#!/bin/python3
import djangorm
from db.models import *

djangorm.migrate()

try:
    alice = User.objects.get(name='Alice')
except:
    alice = User(name='Alice')
    alice.save()

for user in User.objects.all():
    print("ID: %d\tUsername: %s" % (user.id, user.name))
