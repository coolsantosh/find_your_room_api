from django.urls import path
from .views import RoomView , RoomTypeView, RoomDetailView ,RoomStatusView


urlpatterns = [
    path('room/', RoomView.as_view()),
    path('room-type/', RoomTypeView.as_view()),
    path('room-status/', RoomStatusView.as_view()),
    path('room/<uuid:pk>/',RoomDetailView.as_view()),
]
