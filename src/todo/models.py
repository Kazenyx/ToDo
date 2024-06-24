from django.db import models

# Create your models here.

class Todo(models.Model):
  name = models.CharField(max_length=100,)
  created = models.DateTimeField(auto_now_add=True)
  is_enable = models.BooleanField(null=True)

  def __str__(self):
    return str(self.name)