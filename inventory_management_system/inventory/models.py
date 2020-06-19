from django.db import models

# Create your models here.
class Device(models.Model):
    Type=models.CharField(max_length=100, blank=False)
    price=models.IntegerField()
    choices=(
        ('AVAILABLE','Item ready to be purchased'),
        ('SOLD','Item sold'),
        ('RESTOCKING','Item restocking in few days')
    )
    
    status=models.CharField(max_length=20, choices=choices, default="Sold")
    issues=models.CharField(max_length=100, default="No issues")


    def __str__(self):
        return 'Type : {0} price : {1}'.format(self.Type, self.price)
    
    class Meta:
       abstract = True

class Laptop(Device):
    pass
class Desktop(Device):
    pass
class Mobile(Device):
    pass
