from django.db import models

# Create your models here.
class fs(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    track_id=models.CharField(max_length=20)
    is_Delete=models.BooleanField(default=False,null=True)

class resiger(models.Model):
    uid=models.IntegerField(max_length=20)
    pwd=models.CharField(max_length=20)
class new_resiger(models.Model):
    uid=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)