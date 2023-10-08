from django.db import models

from django.contrib.auth.models import User

class Student(models.Model):
    name=models.CharField(max_length=100)
    stu_id=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stu_id}'
    


