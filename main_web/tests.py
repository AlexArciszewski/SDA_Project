from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Covidians
# python manage.py test
#EF. Error, Fail-no fail but exception,  "."-passed
#Tests should start from word "test"
# Create your tests here.

User = get_user_model()
class FirstTestCase(TestCase):

    def test_success(self):
        """ Test success assertTrue if passed gives True. example: assert 1 == 1 if the test does not pass a message will be displayed """
        self.assertTrue(True)



    def test_fail(self):
        self.assertTrue(False)



    def test_error(self):
        """ Test with no assertion. An exception appears"""
        raise ValueError("Error has been raised")


class CovidiansTestCase(TestCase):
    """ Test for Covidians model """

    def test_if_info_about_users_in_covid_app_appears(self):
        """ creating a test-user"""
        user = User.objects.create_user(username="test123", email="test123@gmail.com", password="secret")
        response = self.client.force_login(user) # user must be logged-in


class CovidiansModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Covidians.objects.create(name='tester_001', email='tester', tested_positive='yes', shots_taken='1')






