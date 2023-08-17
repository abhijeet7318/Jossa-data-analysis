from django.db import models

class programm(models.Model):
    institute = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    seat_type = models.CharField(max_length=200,default='OPEN')
    gender = models.CharField(max_length=200,default='Gender-Neutral')
    open = models.FloatField(default=1)
    close = models.FloatField(default=99999)
    year = models.FloatField(default=2020)
    roundd =models.IntegerField(default=1)




