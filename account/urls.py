from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="user_register" ),
    path('login/',UserLoginView.as_view(),name="login" ),
    path('district/',DistrictView.as_view(),name="district" ),
    path('city/',DistrictView.as_view(),name="city" ),
]
