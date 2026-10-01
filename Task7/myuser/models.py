from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.username


class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    student_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    def __str__(self):
        return self.student_name