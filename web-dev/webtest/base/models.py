from django.db import models

# Create your models here.

class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    #null means value can't be blank
    description = models.TextField(null=True, blank =True)
    #participants = 
    #auto_now takes a snapshot of participants every time we save the item  
    update = models.DateTimeField(auto_now=True)
    #auto_now_add only take a snapshot the first time we create the instance. 
    created = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return self.name
