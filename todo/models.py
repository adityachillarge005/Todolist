from django.db import models
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title

