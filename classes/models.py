from django.db import models
from accounts.models import CustomUser


class Semester(models.Model):
    name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    


class Class(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
