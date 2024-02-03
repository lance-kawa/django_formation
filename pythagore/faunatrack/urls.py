from django.urls import path
from faunatrack.views import ProjetCreate, ProjetUpdate, ProjetDelete, ProjetList, ObservationCreate

urlpatterns = [
    path('projet/new/', ProjetCreate.as_view(), name='projet_create'),
    path('projet/<int:pk>/edit/', ProjetUpdate.as_view(), name='projet_update'),
    path('projet/<int:pk>/delete/', ProjetDelete.as_view(), name='projet_delete'),
    path('projet/', ProjetList.as_view(), name='projet_list'),
    path('observation/new/', ObservationCreate.as_view(), name='observation_create'),
]