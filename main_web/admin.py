from django.contrib import admin

from .models import Covidians
# Register your models here.
#admin.site.register(Covidians)
from django.contrib import admin
# from .models import Point


@admin.register(Covidians)      #zaciągamy z models
class CovidiansAdmin(admin.ModelAdmin):
    #fields = ["name", "email", "tested_positive", "shots_taken"]
    #exclude = [name] all but not name
    list_display = ["name", "email", "tested_positive", "shots_taken"] #zamiast fields lepszyw ygląd bardziej rozstrzelone w bazie
    list_filter = ("email",) #tu tupla i muszę przecinek zostawić filtrowanie
    search_field = ("email",) ##tu tupla i muszę przecinek zostawić filtrowanie wyszukiwanie


# class PointAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'x', 'y')

# admin.site.register(Point,PointAdmin)