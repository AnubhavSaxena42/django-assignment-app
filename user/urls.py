
from django.urls import path,include
from .views import UserRegistrationView,UserLoginView
from advisor.views import RetrieveAdvisorView
from bookings.views import RetrieveBookingsView,AdvisorBookingView
urlpatterns =[
    path('login/',UserLoginView.as_view(),name='UserLogin'),
    path('register/',UserRegistrationView.as_view(),name='UserRegistration'),
    path('<int:id>/advisor',RetrieveAdvisorView.as_view(),name='RetrieveAdvisorList'),
    path('<str:id>/advisor/<int:a_id>',AdvisorBookingView.as_view(),name='BookAdvisor'),
    path('<str:id>/advisor/booking/',RetrieveBookingsView.as_view(),name='RetrieveUserBookings'),
]

