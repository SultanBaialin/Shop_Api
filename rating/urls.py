from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewCreateAPIView.as_view()),   # api/v1/reviews POST
    path('<int:pk>/', views.ReviewUpdateDeleteApiView.as_view()),
]