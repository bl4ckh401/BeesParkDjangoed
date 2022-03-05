from django.db import models

# Create your models here.


class Tables(models.Model):
    name = models.CharField(unique=True, primary_key=True,
                            default="", max_length=255)
    tableof = models.IntegerField(default=1, null=True)
    reserved = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

    def book(self):
        self.reserved = True
        return self.name+"has been Reserved "


class ReserveTable(models.Model):
    table = models.ForeignKey(Tables, null=True,
                              on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=255, null=True)
    arrival = models.DateTimeField(null=True)

    def __str__(self):
        return self.name+" booked table "+self.table.name
