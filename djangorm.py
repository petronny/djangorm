#!/bin/python3
import os
from django.conf import settings
from django.apps import apps
from django.core.management import execute_from_command_line

# Django specific settings
module_name = 'db'
database = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(module_name, 'db.sqlite3')
}

conf = {
    'INSTALLED_APPS': [
        module_name
    ],
    'DATABASES': {
        'default': database
    }
}

settings.configure(**conf)
apps.populate(settings.INSTALLED_APPS)

def migrate():
    execute_from_command_line(['', 'makemigrations', module_name])
    execute_from_command_line(['', 'migrate', module_name])

def object_to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data
