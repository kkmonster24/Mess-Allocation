from django.db import models
from datetime import datetime

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
    

class Feedback(models.Model):
    uniform_and_punctuality = models.IntegerField()
    cleanliness_and_hygiene = models.IntegerField()
    waste_disposal = models.IntegerField()
    quality_of_ingredients = models.IntegerField()
    overall_satisfaction_of_breakfast = models.IntegerField()
    overall_satisfaction_of_lunch = models.IntegerField()
    overall_satisfaction_of_dinner = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        opi = (self.uniform_and_punctuality + self.cleanliness_and_hygiene + self.waste_disposal + 2*self.quality_of_ingredients + 3*self.overall_satisfaction_of_breakfast + 3*self.overall_satisfaction_of_lunch + 3*self.overall_satisfaction_of_dinner)/(1+1+1+2+3+3+3)
        return str(opi)
        
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    roll = models.IntegerField()
    subscribed_mess_hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='choice_students')
    #feedback = models.IntegerField(blank=True, null=True)
    feedback = models.OneToOneField(Feedback, on_delete=models.CASCADE, related_name='choice_student', null=True, blank=True)
    feedback_given = models.BooleanField(default=False)
    mess_off_dates = models.ManyToManyField(Date, related_name='choice_students', blank=True)
    authent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username