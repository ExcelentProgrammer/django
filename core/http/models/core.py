from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return self.title
