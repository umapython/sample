from django.db import models

# Create your models here.
class Topic(models.Model):
    Question = models.CharField(max_length=350)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Question

class Answertable(models.Model):
    Answer = models.CharField(max_length=350)
    #topicid = models.ForeignKey(Topic,default=1,on_delete=models.set_default)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Answer
