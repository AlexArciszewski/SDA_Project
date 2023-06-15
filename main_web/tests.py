from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Covidians
# python manage.py test
#EF. Error, Fail-no fail but exception,  "."-passed
#Tests should start from word "test"
# Create your tests here.

User = get_user_model()



class CovidiansModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Covidians.objects.create(id=1,name='tester_001', email='tester', tested_positive='yes', shots_taken='1')

    def test_name_label(self):
        covidians = Covidians.objects.get(id=1)
        field_label = covidians._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_lenght(self):
        covidians = Covidians.objects.get(id=1)
        max_length = covidians._meta.get_field('name').max_length
        self.assertEqual(max_length, 64)








"""

class Covidians(models.Model):
    name = models.CharField(max_length=64, null=True, blank=False)
    email = models.CharField(max_length=64, null=True, blank=False, unique=True)
    tested_positive = models.CharField(max_length=3, null=True, blank=False, default='YES')
    shots_taken = models.PositiveIntegerField(default=0, blank=False)
    #how_got_virus = models.TextField(default="") OPTIONAL!!!
    user_created_at = models.DateField(default=timezone.now) #more info DateField.auto_now_add OPTIONAL!!!
    user_photo = models.ImageField(upload_to="my_media", null=True, blank=True) #OPTIONAL!!!


    def __str__(self):          #w admin userów wyswietli mi po danych jako str
        return f"{self.id, self.name, self.email, self.tested_positive, self.shots_taken, self.user_photo}"
"""



