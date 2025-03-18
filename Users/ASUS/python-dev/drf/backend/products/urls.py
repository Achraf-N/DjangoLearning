from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.ProductDetailApiView.as_view()),
    path('', views.ProductCreateApiView.as_view()) # localhost:8000/api/
]
