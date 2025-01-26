from django.urls import path
from .views import index, new_animal

urlpatterns = [
    path('', index, name='index'),
    path('animal/new/', new_animal)
]
