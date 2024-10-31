from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../kpaas_task/')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../kpaas_task/crawling/')))
from crawling.models import OTC_Bond
from .serializers import OTC_Bond_Serializer


class OTC_Bond_All(viewsets.ReadOnlyModelViewSet):
    queryset = OTC_Bond.objects.all()
    serializer_class = OTC_Bond_Serializer