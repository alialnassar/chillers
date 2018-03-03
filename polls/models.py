from django.db import models

class User(models.Model):
    #id = models.IntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    
class Chiller(models.Model):
    #id = models.IntegerField()
    status = models.BooleanField()
    temprature = models.FloatField()
    
    def __str__(self):
        return str(self.temprature)
    
    def isActive(self):
        return self.status if "Chiller is active" else "Chiller is inactive"