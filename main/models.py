from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
from tinymce.models import HTMLField


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    # content=models.TextField()
    content = QuillField()
    published = models.DateTimeField("date published", default=timezone.now())

    def __str__(self):
        return self.title
