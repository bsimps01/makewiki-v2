from django.db import models

class CreateForm(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
# Create your models here.
