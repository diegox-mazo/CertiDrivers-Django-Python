from django.urls import path
from instructores.views import create_instructores, InstructorListView, InstructorUpdateView, InstructorDeleteView, InstructorDisplayView

urlpatterns = [
    path('create_instructores/', create_instructores, name='create_instructores'),
    path('display_instructores/', InstructorDisplayView.as_view(), name='display_instructores'), 
    path('list_instructores/', InstructorListView.as_view(), name='list_instructores'),    
    path('update_instructores/<int:pk>/', InstructorUpdateView.as_view(), name='update_instructores'),
    path('delete_instructores/<int:pk>/', InstructorDeleteView.as_view(), name='delete_instructores'),     
]