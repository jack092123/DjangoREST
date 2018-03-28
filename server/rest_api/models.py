from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    status = models.TextField(default='unfinished')
    priority = models.TextField(default='low')
    due_date = models.DateField()
    note = models.TextField(blank=True)
    last_modify = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TodoList"