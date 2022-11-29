from django.urls import path
from . import views

app_name = 'Foodie_app' # for namespacing
urlpatterns = [
    path('/', views.index, name='index')
]