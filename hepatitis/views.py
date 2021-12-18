from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Hepatitis
from .permissions import IsOwnerOrReadOnly
from .serializers import HepatitisSerializers


@csrf_exempt
def Hepatitis_Create(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        name = data["name"]
        email = data["email"]
        mobile = data["mobile"]
        age = data["age"]
        gender = data["gender"]
        steroid = data["steroid"]
        antivirals = data["antivirals"]
        fatigue = data["fatigue"]
        malaise = data["malaise"]
        anorexia = data["anorexia"]
        liver_big = data["liver_big"]
        liver_firm = data["liver_firm"]
        spleen_palpable = data["spleen_palpable"]
        spiders = data["spiders"]
        ascites = data["ascites"]
        varices = data["varices"]
        bilirubin = data["bilirubin"]
        alk_phosphate = data["alk_phosphate"]
        sgot = data["sgot"]
        albumin = data["albumin"]
        protime = data["protime"]
        histology = data["histology"]

        collection = []
        collection += [
            age,
            gender,
            steroid,
            antivirals,
            fatigue,
            malaise,
            anorexia,
            liver_big,
            liver_firm,
            spleen_palpable,
            spiders,
            ascites,
            varices,
            bilirubin,
            alk_phosphate,
            sgot,
            albumin,
            protime,
        ]

        from .predictor import AIModel

        instance = AIModel()
        predicted_status = instance.predict(collection)
        print(predicted_status)

        if predicted_status == 0:
            predicted_status = "Negative"
        elif predicted_status == 1:
            predicted_status = "Positve"
        else:
            predicted_status = "Unkown"

        Hepatitis.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            age=age,
            gender=gender,
            steroid=steroid,
            antivirals=antivirals,
            fatigue=fatigue,
            malaise=malaise,
            anorexia=anorexia,
            liver_big=liver_big,
            liver_firm=liver_firm,
            spleen_palpable=spleen_palpable,
            spiders=spiders,
            ascites=ascites,
            varices=varices,
            bilirubin=bilirubin,
            alk_phosphate=alk_phosphate,
            sgot=sgot,
            albumin=albumin,
            protime=protime,
            histology=histology,
            status=predicted_status,
        )

        return JsonResponse(data, status=status.HTTP_201_CREATED)


class HepatitisList(ListCreateAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticatedOrReadOnly,
    )
    model = Hepatitis
    serializer_class = HepatitisSerializers
    queryset = Hepatitis.objects.all()


class HepatitisDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    model = Hepatitis
    serializer_class = HepatitisSerializers
    queryset = Hepatitis.objects.all()
