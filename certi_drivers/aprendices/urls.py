from django.urls import path
from aprendices.views import create_aprendices, AprendizListView, AprndizUpdateView, AprendizDeleteView

urlpatterns = [
    path('create_aprendices/', create_aprendices, name='create_aprendices'),
    path('list_aprendices/', AprendizListView.as_view(), name='list_aprendices'),    
    path('update_aprendices/<int:pk>/', AprndizUpdateView.as_view(), name='update_aprendices'),
    path('delete_aprendices/<int:pk>/', AprendizDeleteView.as_view(), name='delete_aprendices'),
]