#!/bin/python3
import os
import sys
from django.conf import settings
from django.apps import apps
from django.core.management import execute_from_command_line
from django.db.models import ManyToManyField


class DjangORM:

    def __init__(self, module_name, database=None, module_path='.'):
        if database is None:
            module_path = os.path.join(os.path.join(os.path.dirname(sys.argv[0]), module_path), module_name)
            if os.path.exists(module_path) is False:
                os.makedirs(module_path)
            database = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(module_path, 'db.sqlite3')
            }
        if not isinstance(module_name, str):
            raise ValueError
        if not isinstance(database, dict):
            raise ValueError

        self.module_name = module_name
        self.database = database
        self.__configured__ = False

    def configure(self):
        if self.__configured__:
            return
        configuration = {
            'INSTALLED_APPS': [
                self.module_name
            ],
            'DATABASES': {
                'default': self.database
            }
        }
        settings.configure(**configuration)
        apps.populate(settings.INSTALLED_APPS)
        self.__configured__ = True

    def migrate(self):
        if self.__configured__ is False:
            self.configure()
        execute_from_command_line(['', 'makemigrations', self.module_name])
        execute_from_command_line(['', 'migrate', self.module_name])

    @staticmethod
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
