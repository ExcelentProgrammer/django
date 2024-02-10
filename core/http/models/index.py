from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = RichTextField()
    image = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return self.title
