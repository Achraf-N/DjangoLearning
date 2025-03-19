from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.Product_alt_View),
    path('', views.Product_alt_View) # localhost:8000/api/
]
