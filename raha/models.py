from django.db import models
from  django.contrib.auth.models import User 

class Topic(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,default=1)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment
