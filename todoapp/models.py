from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    details=models.TextField(max_length=200)
    status=models.CharField(max_length=30)


    def __str__(self):
        return self.status
