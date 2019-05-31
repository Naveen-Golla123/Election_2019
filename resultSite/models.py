from django.db import models

# Create your models here.

class consistencyLS(models.Model):
    consistency = models.CharField(max_length=40)
    winner= models.CharField(max_length=100)
    winparty=models.CharField(max_length=40)
    trailer= models.CharField(max_length=100)
    trailparty=models.CharField(max_length=40)
    margin= models.CharField(max_length=40)


class consistencyAC(models.Model):
    consistency = models.CharField(max_length=40)
    winner= models.CharField(max_length=100)
    winparty=models.CharField(max_length=40)
    trailer= models.CharField(max_length=100)
    trailparty=models.CharField(max_length=40)
    margin= models.CharField(max_length=40)
    district=models.PositiveIntegerField(default=0)
    partycolor=models.PositiveIntegerField(default=0)
