from django.db import models

# Create your models here.

class Notes(models.Model):
    noteTitle = models.CharField(max_length=100)
    noteContent = models.CharField(max_length=300)
    noteId = models.AutoField(primary_key=True)
