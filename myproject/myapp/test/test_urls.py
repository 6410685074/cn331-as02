
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from myapp.views import index,about,user_login,user_logout,regis,account_reg
class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func,index)

    def test_about_url_is_resolved(self):
        url=reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)
    
    def test_login_url_is_resolved(self):
        url=reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,user_login)

    def test_logout_url_is_resolved(self):
        url=reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func,user_logout)
    
    def test_regis_url_is_resolved(self):
        url=reverse('regis')
        print(resolve(url))
        self.assertEquals(resolve(url).func,regis)

    def test_account_url_is_resolved(self):
        url=reverse('account_reg')
        print(resolve(url))
        self.assertEquals(resolve(url).func,account_reg)