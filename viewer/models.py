# viewer/models.py
from django.db import models

class Model3D(models.Model):
    name = models.CharField(max_length=255)  # Name of the model
    file = models.FileField(upload_to='models/')  # Upload directory
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.name
