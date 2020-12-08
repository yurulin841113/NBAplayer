from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.URLField(blank=True)
    body = models.TextField()
    photo = models.URLField(blank=True)
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return self.title
