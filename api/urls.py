from django.urls import path
from .views import AdvertAPIView, AdvertDetailView

urlpatterns = [
    path('advert-list/', AdvertAPIView.as_view()),
    path('advert/<int:pk>/', AdvertDetailView.as_view()),
]
