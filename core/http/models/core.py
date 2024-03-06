from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class Comment(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.text


class BaseComment(PolymorphicModel):
    comments = models.ManyToManyField(Comment)


class Post(BaseComment):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return self.title


class FrontendTranslation(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name_plural = _("Frontend Translations")
        verbose_name = _("Frontend Translation")
