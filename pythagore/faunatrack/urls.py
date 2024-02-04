from django.urls import path
from faunatrack.views import ProjetCreate, ProjetList

urlpatterns = [
    path('projet/new/', ProjetCreate.as_view(), name='projet_create'),
    path('projet/', ProjetList.as_view(), name='projet_list'),
]