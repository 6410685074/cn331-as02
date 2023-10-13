from django.db import models

from django.contrib.auth.models import User

class Student(models.Model):
    student_house=models.CharField(max_length=100)
    stu_id=models.OneToOneField(User,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=40)
    student_img=models.ImageField(null=True,blank=True,upload_to='images/')
    def __str__(self):
        return f'{self.stu_id}'
    
