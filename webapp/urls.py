
from django.urls import path, include
from .views import *



# Add other URLs of your project
urlpatterns = [
    path('', home, name='home'),
]

# Ajoutez les URLs générées
urlpatterns += generate_crud_views()