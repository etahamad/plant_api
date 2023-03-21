from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .models import PlantInformation
from .serializers import PlantInformationSerializer


class CreatePlantInformationAPIView(CreateAPIView):
    """
    create plant information instance
    """
    queryset = PlantInformation.objects.all()
    serializer_class = PlantInformationSerializer


class ListPlantInformationAPIView(ListAPIView):
    """
    return List of Plant Information's
    """
    queryset = PlantInformation.objects.all()
    serializer_class = PlantInformationSerializer


class RetrievePlantInformationAPIView(RetrieveAPIView):
    """
    return plant information instance
    by a given plant information id
    """
    queryset = PlantInformation.objects.all()
    serializer_class = PlantInformationSerializer
    lookup_field = 'id'


class DeletePlantInformationAPIView(DestroyAPIView):
    """
    delete plant information instance
    by a given plant information id
    """
    queryset = PlantInformation.objects.all()
    serializer_class = PlantInformationSerializer
    lookup_field = 'id'
