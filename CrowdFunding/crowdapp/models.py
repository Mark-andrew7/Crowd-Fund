from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
  USER_TYPES = (
    ('investor', 'Investor'),
    ('advisor', 'Advisor'),
    ('business', 'Business')
  )
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_type = models.CharField(max_length=100, choices=USER_TYPES)
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  amount = models.IntegerField()
  investment_type = models.CharField(max_length=100)


class investment(models.Model):
  name = models.CharField(max_length=100)
  investor = models.ForeignKey('User', on_delete=models.CASCADE)
  description = models.CharField(max_length=100)
  value_per_share = models.FloatField()
  is_approved = models.BooleanField(default=False)
  investment_type = models.CharField()
  valuation = models.FloatField()
  amount = models.IntegerField()


class shares(models.Model):
  investor = models.ForeignKey('User', on_delete=models.CASCADE)
  advisor = models.ForeignKey('User', on_delete=models.CASCADE)
  investment = models.ForeignKey('investment', on_delete=models.CASCADE)
  value = models.IntegerField()
  
