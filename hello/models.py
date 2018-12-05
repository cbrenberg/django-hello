from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Todo(models.Model):
    todo_item = models.CharField(max_length=250)
    is_complete = models.BooleanField(default=False)
    due_date = models.DateField('due date', default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo_item
