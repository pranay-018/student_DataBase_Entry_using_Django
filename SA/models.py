from django.db import models
from django.db import models
# Create your models here.
class stumodel(models.Model):
    s_name=models.CharField(max_length=30)
    s_regno=models.IntegerField()
    s_m1=models.FloatField()
    s_m2=models.FloatField()
    def __str__(self):
        return str(self.s_name)    