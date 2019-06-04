#!/bin/python3
from djangorm import DjangORM
test_db = DjangORM(module_name='test')
test_db.configure()
test_db.migrate()

from test.models import *

try:
    alice = User.objects.get(name='Alice')
except:
    alice = User(name='Alice')
    alice.save()

for user in User.objects.all():
    print("ID: %d\tUsername: %s" % (user.id, user.name))
