from django.db import models

class Client(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Mname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(max_length=100)
    group = models.CharField(max_length=100)
    country = models.CharField(max_length=125)

    def __str__(self):
        return self.Lname + "   " + self.Fname + "   " + self.Mname