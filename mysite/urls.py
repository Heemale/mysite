
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    # path('eggs/',views.eggs),
    path('count/',views.count,name='count'),
    path('about/',views.about,name='about'),
]
