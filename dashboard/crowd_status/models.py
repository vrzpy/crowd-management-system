from turtle import ondrag
from django.db import models

# Create your models here.
class StationInfo(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.id} {self.Name} {self.Code}"

class StationDensity(models.Model):
    Station = models.OneToOneField(StationInfo,on_delete=models.CASCADE)
    Density = models.FloatField()

    def __str__(self) -> str:
        return f"{self.Station} {self.Density}"

class TrainDensity(models.Model):
    TowardsStation = models.ForeignKey(StationInfo, on_delete=models.CASCADE, related_name='TowardsStation')
    CurrentStation = models.ForeignKey(StationInfo, on_delete=models.CASCADE, related_name='CurrentStation')
    Density = models.FloatField()

    def __str__(self) -> str:
        return f"{self.TowardsStation} {self.CurrentStation} {self.Density}"

class NewsFeed(models.Model):
    News = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.News[:50]}"