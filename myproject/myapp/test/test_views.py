from django.test import TestCase,Client
from django.urls import reverse
from myapp.models import Student
from courses.models import Course,Regis
import json
from django.contrib.auth.models import User

from django.core.files.uploadedfile import SimpleUploadedFile


class TestViews(TestCase):
    
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('index')
        self.about_url=reverse('about')
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')
        self.regis_url=reverse('regis')
        self.account_url=reverse('account_reg')
        """self.user=User.objects.create_user("6410685099","stu_ajarnjack")
        self.client.login(username="6410685099",password="stu_ajarnjack")
        self.course1 = Course.objects.create(ID='cn339', name='Math 101', num=20, nItems=10, lecturer='John Doe', status=True, info='Course info', sem_year='2023')
        self.course2 = Course.objects.create(ID='cn338', name='Science 202', num=15, nItems=5, lecturer='Jane Smith', status=True, info='Course info', sem_year='2023')
        self.student = Student.objects.create(student_house='Gryffindor', stu_id=self.user,student_name="abut to klam")
        self.regis = Regis.objects.create(stu_id=self.user, c_id=self.course1)"""

    def test_index_url_get(self):
        response=self.client.get(self.index_url)
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"index.html")
    
    def test_about_url_get(self):
        response=self.client.get(self.about_url)
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"about.html")
    
    def test_login_url_get(self):
        response=self.client.get(self.login_url)
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"userlogin.html")
    
    def test_logout_url_get(self):
        response=self.client.get(self.logout_url)
        print(response)
        self.assertIn(response.status_code,[200,302])
    
    def test_regis_url_get(self):
        
        response=self.client.get(self.regis_url)
        self.assertIn(response.status_code,[200,302])
        self.assertTemplateUsed(response,'regis.html')
        
        

    def test_login_POST(self):
        self.user=User.objects.create_user(username="aaa",password="aaa")
        response=self.client.post(self.login_url,{
            'username':"aaa",
            'password':"aaa",
        })
        print(response)
        self.assertIn(response.status_code, [200, 302])
        self.user = response.wsgi_request.user
        self.assertTrue(self.user.is_authenticated)

    def test_logout_POST(self):
        self.user=User.objects.create_user(username="aaa",password="aaa")
        response=self.client.get(self.logout_url,follow=True)
        self.assertEqual(response.status_code,200)
        self.user=response.wsgi_request.user
        self.assertFalse(self.user.is_authenticated)

"""    def test_account_url_get(self):
        r=Regis.objects.first()
        response=self.client.get(self.account_url,args=(r.c_id))
        self.assertIn(response.status_code,[200,302])
        self.assertTemplateUsed(response,'account_reg.html')"""