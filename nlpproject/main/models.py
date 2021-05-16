from django.db import models
import os

# Create your models here.
class Document(models.Model):
    document_file = models.FileField(upload_to='main/documents/')

    def __str__(self):
        return os.path.basename(self.document_file.name)
