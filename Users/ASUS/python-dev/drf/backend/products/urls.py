from . import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_delete_view),
    path('', views.product_list_view) # localhost:8000/api/
]
