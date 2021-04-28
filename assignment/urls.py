
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('adminsite/',admin.site.urls),
    path('admin/',include('advisor.urls')),
    path('user/',include('user.urls')),
]
