from django.db import models

# Create your models here.

class Date(models.Model):
    date = models.DateField()
    
    def __str__(self):
        return self.date

    
class Hostel(models.Model):
    name = models.CharField(max_length=20)
    rating = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    roll = models.IntegerField()
    subscribed_mess_hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='choice_students')
    feedback = models.IntegerField(blank=True, null=True)
    feedback_given = models.BooleanField(default=False)
    mess_off_dates = models.ManyToManyField(Date, related_name='choice_students', blank=True)
    authent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username