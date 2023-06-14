from django.db.models import Count
from django.db.models.functions import Trunc
from django.utils import timezone

from django.db import models


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

    #def name_tested_positive(self): #inny wygląd
        #return f"{self.name} ({self.tested_positive})"
    #jak to wywołać problem z wywołaniem


    #objects_per_date = Covidians.objects.annotate(created_date=Trunc('user_created_at', 'date')).values(
    #    'created_date').annotate(count=Count('id'))
