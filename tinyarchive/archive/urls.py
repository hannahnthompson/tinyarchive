from django.urls import path
from archive import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.item_detail)
]