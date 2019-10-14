from django.db import models

class remaindtbl(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default=00)
    quotes = models.CharField(max_length=20, default=00)
    date = models.CharField(max_length=20, default=00)
    subject = models.CharField(max_length=2000)
    loginuser=models.CharField(max_length=20, default=00)
class usertable(models.Model):
    name = models.CharField(max_length=20, default=00)

    password = models.CharField(max_length=20, default=00)

