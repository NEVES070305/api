from django.db import models

# Create your models here.

class JSONCLP(models.Model):
    Sensor = models.BooleanField(blank=False, null=False)
    Button = models.BooleanField(blank=False, null=False)
    TurnOn = models.BooleanField(blank=False, null=False)
    ResetCount = models.BooleanField(blank=False, null=False)
    CountValue = models.IntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return "JSON CLP"
    
     