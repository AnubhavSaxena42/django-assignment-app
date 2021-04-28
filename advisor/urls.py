from django.urls import path,include
from .views import AdvisorRegistrationView
urlpatterns = [
    path('advisor/',AdvisorRegistrationView.as_view(),name='advisorRegistration')
]
