from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cancer
from .serializers import CancerSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
def Cancer_Create(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        name = data["name"]
        email = data["email"]
        age = data["age"]
        texture_mean = data["texture_mean"]
        area_mean = data["area_mean"]
        smoothness_mean = data["smoothness_mean"]
        compactness_mean = data["compactness_mean"]
        concavity_mean = data["concavity_mean"]
        concave_points_mean = data["concave_points_mean"]
        state = data["state"]

        Cancer.objects.create(
            name=name,
            email=email,
            age=age,
            texture_mean=texture_mean,
            area_mean=area_mean,
            smoothness_mean=smoothness_mean,
            compactness_mean=compactness_mean,
            concavity_mean=concavity_mean,
            concave_points_mean=concave_points_mean,
            state=state,
        )

        return JsonResponse(data, status=status.HTTP_201_CREATED)


class CancerList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Cancer.objects.all()
    serializer_class = CancerSerializer


class CancerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Cancer.objects.all()
    serializer_class = CancerSerializer
