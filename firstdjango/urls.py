from django.contrib import admin
from django.urls import path,include

from first import views #first package 내의 views.py 불러옴

urlpatterns = [
    path('', include('first.urls')), #name은 classname같은 것
    path('admin/', admin.site.urls),
]
