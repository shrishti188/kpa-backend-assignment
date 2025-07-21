from django.db import models
class BmbcChecksheet(models.Model):
    adjustingTube = models.CharField(max_length=100)
    cylinderBody = models.CharField(max_length=100)
    bracket = models.CharField(max_length=100)

class WheelAssembly(models.Model):
    leftWheel = models.CharField(max_length=100)
    rightWheel = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    bmbcChecksheet = models.OneToOneField(BmbcChecksheet, on_delete=models.CASCADE)
    wheelAssembly = models.OneToOneField(WheelAssembly, on_delete=models.CASCADE)
    remarks = models.TextField()
    inspectedBy = models.CharField(max_length=100)
class WheelSpecification(models.Model):
    wheelType = models.CharField(max_length=100)
    diameter = models.FloatField()
    material = models.CharField(max_length=100)

    def __str__(self):
       return self.wheelType
