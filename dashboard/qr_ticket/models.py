from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TicketPricing(models.Model):
    Source = models.CharField(max_length = 100, blank=False, null=False)
    Destination = models.CharField(max_length = 100, blank=False, null=False)
    Price = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.Source} to {self.Destination} @ {self.Price}"

class TicketHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Source = models.CharField(max_length = 100, blank=False, null=False)
    Destination = models.CharField(max_length = 100, blank=False, null=False, default='None')
    Price = models.PositiveIntegerField(default=0, null=True, blank=True)
    JourneyDateTime = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.Source} to {self.Destination} @ {self.Price}"
