from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.title
