from typing import Any
from django.db import models
import os
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    
    cover = models.ImageField(upload_to='book_covers')
    file = models.FileField(upload_to='books')

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        cover_path = os.path.join(settings.MEDIA_ROOT, self.cover.name)
        file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
        if os.path.exists(file_path):
            os.remove(file_path)
            
        if os.path.exists(cover_path):
            os.remove(cover_path)
        super().delete(*args, **kwargs)

