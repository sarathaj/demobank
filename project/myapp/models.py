from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.uname},{self.id}'

    #
    # def __str__(self):
    #     return self.fname


# Create your models here.
class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    pin = models.IntegerField()
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    #pwd = models.CharField(max_length=100)

