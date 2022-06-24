from django.db import models

class Collection(models.Model):
    photo=models.ImageField(upload_to='image')
    created_at=models.DateTimeField(auto_now_add=True)