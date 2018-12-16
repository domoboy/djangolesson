from django.urls import path
from main.views import (main_view, contacts_view, prod_view, prod_deails_view)

urlpatterns = [
    path('', main_view),
    path('contacts/', contacts_view),
    path('product-deails/', prod_deails_view),
    path('products/', prod_view),
]