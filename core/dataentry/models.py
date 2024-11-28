from django.db import models




class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name    = models.CharField(max_length=50)
    age     = models.IntegerField()
    
    
    def __str__(self) -> str:
        return str(self.name)
    
    
    
class CSVDate(models.Model):
    gender = models.CharField(max_length=10)
    race   = models.CharField(max_length=20)
    parental_level_of_education = models.CharField(max_length=20)
    lunch  = models.CharField(max_length=20)
    test_preparation_course = models.CharField(max_length=10)
    math_score = models.DecimalField(max_digits=6, decimal_places=2)
    reading_score = models.DecimalField(max_digits=6, decimal_places=2)
    writing_score = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self) -> str:
        return str(self.race)
    
    
    

class Customer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)    
    
    def __str__(self) -> str:
        return str(self.name)