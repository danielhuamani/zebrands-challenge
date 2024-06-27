from django.core.exceptions import FieldError
from django.db import models


class RemovedQuerySet(models.QuerySet):
    def removed(self):
        return self.filter(is_removed=False)


class RemovedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_removed=False)


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class ActiveRemovedManager(models.Manager):
    def get_queryset(self):
        try:
            return super().get_queryset().filter(is_removed=False, is_active=True)
        except FieldError:
            return super().get_queryset().filter(is_removed=False)


class ActiveRemovedQuerySet(models.QuerySet):
    def get_queryset(self):
        try:
            return super().get_queryset().filter(is_removed=False, is_active=True)
        except FieldError:
            return super().get_queryset().filter(is_removed=False)


