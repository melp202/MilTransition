from django.db import models

# Create your models here.
# STATE MODEL
class State(models.Model):
    name = models.CharField(max_length=100)
    state_flag = models.TextField()

    def __str__(self):
        self.name

# ORGANIZATION MODEL
class Organization(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=100, default='no name')
    industry = models.CharField(max_length=100, default='no specified industry')
    image = models.TextField(default='no org. image')
    description = models.TextField(default='no org. descrition')
    external_link = models.TextField(default='no external link')

    def __str__(self):
        return self.name