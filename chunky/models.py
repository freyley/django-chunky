from django.db import models


class Chunk(models.Model):
    slug = models.CharField(unique=True, max_length=255)
    content = models.TextField(default="THIS CHUNK HAS NO CONTENT")

    def __unicode__(self):
        return self.slug
