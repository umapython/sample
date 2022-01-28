from django.contrib import admin
from django.urls import path
from . import views
app_name = "wwcodeapp"

urlpatterns = [
    path('index/',views.index, name='index'),
    path('details/',views.details, name='details'),
    path('cards/',views.cards, name='cards'),
    path('cards/id=<int:id>',views.cards, name='cards'),
    path('datas/',views.datas, name='datas'),
]