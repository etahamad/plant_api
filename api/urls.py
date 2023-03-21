from django.urls import path
from .views import (
    CreatePlantInformationAPIView,
    ListPlantInformationAPIView,
    RetrievePlantInformationAPIView,
    DeletePlantInformationAPIView
)

urlpatterns = [
    path('create-plant-info', CreatePlantInformationAPIView.as_view()),
    path('list-plants-info', ListPlantInformationAPIView.as_view()),
    path('get-plant-info/<int:id>', RetrievePlantInformationAPIView.as_view()),
    path('delete-plant-info/<int:id>', DeletePlantInformationAPIView.as_view()),
]
