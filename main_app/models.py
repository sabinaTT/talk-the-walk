from django.db import models

# Create your models here.
class Stack(models.Model):
    name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Question(models.Model):
    the_question = models.CharField(max_length=100)
    answer = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.the_question

    class Meta:
        ordering = ['created_at']





