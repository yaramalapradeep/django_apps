from django.db import models

class TodoListItem(models.Model):
    content = models.CharField(max_length=100)
    status=models.CharField(max_length=30)
