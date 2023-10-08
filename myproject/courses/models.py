from django.contrib.auth.models import User

from django.db import models

class Course(models.Model):
    ID = models.CharField(max_length=5,primary_key=True)
    name = models.CharField(max_length=40)
    num = models.IntegerField()
    nItems= models.IntegerField(default=0)
    lecturer=models.CharField(max_length=100)
    status=models.BooleanField()
    info=models.TextField(max_length=3000)
    lecturer_img=models.ImageField(null=True,blank=True,upload_to='images/')
    
    def __str__(self):
        return f'{self.ID}'
    def get_c_id(self):
        return self.ID


class Regis(models.Model):
    stu_id = models.ForeignKey(User, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.c_id} {self.stu_id}'
    
    def get_c_id(self):
        return self.c_id
    
    def get_stu_id(self):
        return self.stu_id