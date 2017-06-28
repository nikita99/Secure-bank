from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Accounts(models.Model):
    user=models.ForeignKey(User)
    account_no = models.IntegerField(blank=False,null=False)
    balance = models.IntegerField(blank=False,null=False, default=1000)
   # account_date = models.DateTimeField(blank=True,null=False)


    # def account_d(self):
    #      self.account_date = timezone.now()
    #      self.save()

    def __int__(self):
         return self.account_no























