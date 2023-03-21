from rest_framework.serializers import ModelSerializer
from .models import PlantInformation


class PlantInformationSerializer(ModelSerializer):
    class Meta:
        model = PlantInformation
        fields = '__all__'
