from django.db import models
import uuid
# Create your models here.


class Trip(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True) #one trip has many tag and vice versa
    vote_total = models.IntegerField(default=0, null=True, blank=True)# all the vote that the trips has
    vote_ration = models.IntegerField(default=0, null=True, blank=True)# the ration betwen negative and positive
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    def __str__(self): 
        return self.title

class Review(models.Model): 
    VOTE_TYPE = ( 
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner =
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices= VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self): 
        return self.value

class Tag(models.Model): 
    name = models.CharField(max_length=200) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self): 
        return self.name