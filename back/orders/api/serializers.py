from rest_framework.serializers import ModelSerializer
from orders.models import Color

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
