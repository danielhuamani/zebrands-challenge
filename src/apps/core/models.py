from django.db import models
from django.utils.translation import gettext_lazy as _
from uuslug import uuslug

from .managers import ActiveManager, ActiveRemovedManager, RemovedManager


class CoreTimeModel(models.Model):
    """ Modelo Base"""
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        abstract = True


class CoreActiveModel(models.Model):
    """Modelo Activo"""
    is_active = models.BooleanField(_('is active'), default=True)
    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        abstract = True


class CorePositionModel(models.Model):
    """Modelo Posicion"""
    position = models.IntegerField(_('Position'), default=1)

    class Meta:
        verbose_name = "CorePositionModel"
        verbose_name_plural = "CorePositionModels"
        abstract = True
        ordering = ['position']


class CoreSeoSlugModel(models.Model):
    slug = models.CharField(max_length=120, blank=True)
    title = models.CharField(_("title"), max_length=120, blank=True)
    meta_description = models.CharField(_('description'), max_length=255,
                                        blank=True)

    class Meta:
        verbose_name = "CoreSeoSlugModel"
        verbose_name_plural = "CoreSeoSlugModel"
        abstract = True

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = uuslug(self.slug, instance=self, slug_field='slug', filter_dict=None)
        super(CoreSeoSlugModel, self).save(*args, **kwargs)


class CoreRemovedModel(models.Model):
    is_removed = models.BooleanField(default=False)
    remove_objects = RemovedManager()
    active_remove_objects = ActiveRemovedManager()

    class Meta:
        verbose_name = "Delete Model"
        verbose_name_plural = "Delete Models"
        abstract = True

    def __str__(self):
        pass


