from django.db import models


# Create your models here.
class Servis(models.Model):
    ism = models.CharField(max_length=50)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='media')
    sana = models.DateField(auto_now=True)


class Web(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi


class Portfolio(models.Model):
    ism = models.CharField(max_length=50)
    web = models.ForeignKey(Web, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    sana = models.DateField(auto_now=True)


class Team(models.Model):
    ism = models.CharField(max_length=50)
    lavozimi = models.CharField(max_length=50)
    malumot = models.TextField()
    insta = models.CharField(max_length=30)
    tg = models.CharField(max_length=30)
    twit = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    rasm = models.ImageField(upload_to='media')
    sana = models.DateField(auto_now=True)

class Contact(models.Model):
    ism = models.CharField(max_length=50)
    yonalish = models.CharField(max_length=60)
    malumot = models.TextField()
    email = models.CharField(max_length=30)