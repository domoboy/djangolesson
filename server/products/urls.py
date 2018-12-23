from django.urls import path
from .views import detail_view, list_view

app_name = 'products'

urlpatterns = [
    path('', list_view, name='products'),
    path('<int:pk>/', detail_view, name='detail'),
]
