from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    #room 
    name = models.CharField(max_length=200)

def __str__(self):
    return self.name


#CASCADE: When the referenced object is deleted, also delete the objects that have references to it 
# (when you remove a blog post for instance, you might want to delete comments as well). 
# SQL equivalent: CASCADE.


#SET_NULL: Set the reference to NULL (requires the field to be nullable).
#  For instance, when you delete a User, you might want to keep the comments he posted on blog posts,
#  but say it was posted by an anonymous (or deleted) user.
#  SQL equivalent: SET NULL.

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null =True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
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


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #describes the entity we want to point to. on_delete 
    #instead describes how the database should behave when the "one" side of the relationship is deleted. 
    # When the "one" entity is deleted, with CASCADE the "many" 
    # entities are deleted as well.
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[0:50] 




    
