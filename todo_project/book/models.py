from django.db import models

class BookStoreModel(models.Model):   
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=90,null=True)
    taskDescription = models.CharField(max_length=190,null=True)
    is_completed = models.BooleanField(default=False)