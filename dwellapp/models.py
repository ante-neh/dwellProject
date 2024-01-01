from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    student_class = models.CharField(max_length=20)
    grade = models.CharField(max_length=3)
    subjects = models.JSONField()
