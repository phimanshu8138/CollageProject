from django.db import models


# Create your models here.

class Regis_db(models.Model):
    name = models.CharField(max_length=25)
    emailid = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class donate_db(models.Model):
    Category = models.CharField(max_length=25)
    Book_Name = models.CharField(max_length=40)
    Author_Name = models.CharField(max_length=25)
    Donater_name = models.CharField(max_length=25)
    Mob_no = models.IntegerField(max_length=25)
    Email_id = models.CharField(max_length=25)
    Select_State = models.CharField(max_length=25)
    City_name = models.CharField(max_length=25)
    filename = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.Donater_name


class contact_db(models.Model):
    Your_name = models.CharField(max_length=25)
    Email_Address = models.CharField(max_length=25)
    Mobile_No = models.CharField(max_length=25)
    Message = models.CharField(max_length=250)

    def __str__(self):
        return self.Your_name
