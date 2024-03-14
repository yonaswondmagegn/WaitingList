from .models import Form
from rest_framework.serializers import ModelSerializer

class FormSerializer(ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"