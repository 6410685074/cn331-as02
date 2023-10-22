from django.test import TestCase,Client
from django.urls import reverse
from myapp.models import Student
from courses.models import Course,Regis
import json
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        self.user=User.objects.create_user("6410685999","6410685999@gmail.com","stu_ajarnjack")
        self.student1 = Student.objects.create(stu_id=self.user,student_house='Gryffindor',student_name="harry kane")
        self.course1 = Course.objects.create(ID='cn339', name='Math 101', num=20, nItems=10, lecturer='John Doe', status=True, info='Course info jaa', sem_year='2023')
        self.course2 = Course.objects.create(ID='cn338', name='Science 202', num=15, nItems=15, lecturer='Jane Smith', status=True, info='Course info jaa2', sem_year='2023')
        self.course3=Course.objects.create(ID='cn337',name='x',num=10,nItems=4,lecturer='non',status=False,info="ghadsf",sem_year='2023')
    
    def test_value_c1(self):
        self.assertEqual(self.course1.ID,'cn339')
        self.assertEqual(self.course1.name,'Math 101')
        self.assertEqual(self.course1.num,20)
        self.assertTrue(self.course1.status)

    def test_value_c2(self):
        self.assertEqual(self.course2.ID,'cn338')
        self.assertEqual(self.course2.num,self.course2.num)
    
    def test_value_c3(self):
        self.assertEqual(self.course3.ID,'cn337')
        self.assertFalse(self.course3.status)

    def test_model_relations(self):
        self.regis1=Regis(stu_id=self.user,c_id=self.course1)
        self.assertEqual(self.regis1.stu_id,self.student1.stu_id)
        self.assertEqual(self.regis1.c_id,self.course1)
        self.assertEqual(self.regis1.c_id.ID,self.course1.ID)
        
    
        

        