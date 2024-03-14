from django.shortcuts import render
from .models import Form
from .serializers import FormSerializer
from rest_framework.viewsets import ModelViewSet


class FormViewSet(ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
