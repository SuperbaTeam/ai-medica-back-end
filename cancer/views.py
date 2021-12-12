from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cancer
from .serializers import CancerSerializer


class CancerList(ListCreateAPIView):
    queryset = Cancer.objects.all()
    serializer_class = CancerSerializer


class CancerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cancer.objects.all()
    serializer_class = CancerSerializer