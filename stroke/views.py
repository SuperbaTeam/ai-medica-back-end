from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Stroke
from .permissions import IsOwnerOrReadOnly
from .serializers import StrokeSerializers


@csrf_exempt
def Stroke_Create(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        name = data["name"]
        email = data["email"]
        mobile = data["mobile"]
        age = data["age"]
        bmi = data["bmi"]
        avg_glucose_level = data["avg_glucose_level"]
        gender = data["gender"]
        residence_type = data["residence_type"]
        ever_married = data["ever_married"]
        work_type = data["work_type"]
        smoking_status = data["smoking_status"]
        hypertension = data["hypertension"]
        heart_disease = data["heart_disease"]

        collection = []
        collection += [
            age,
            bmi,
            avg_glucose_level,
            gender,
            ever_married,
            residence_type,
            heart_disease,
            hypertension,
        ]
        smoking_status = smoking_status.split(",")
        work_type = work_type.split(",")
        modified_colloection = []
        for item in smoking_status:
            collection += [item]
        for item in work_type:
            collection += [item]
        for item in collection:
            modified_colloection.append(float(item))
        from .predictor import AIModel

        instance = AIModel()
        predicted_status = instance.predict(modified_colloection)

        if predicted_status == 0:
            predicted_status = "Negative"
        elif predicted_status == 1:
            predicted_status = "Positve"
        else:
            predicted_status = "Unkown"

        Stroke.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            age=age,
            bmi=bmi,
            gender=gender,
            avg_glucose_level=avg_glucose_level,
            residence_type=residence_type,
            ever_married=ever_married,
            work_type=work_type,
            smoking_status=smoking_status,
            hypertension=hypertension,
            heart_disease=heart_disease,
            status=predicted_status,
        )

        return JsonResponse(data, status=status.HTTP_201_CREATED)


class StrokeList(ListCreateAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticatedOrReadOnly,
    )
    model = Stroke
    serializer_class = StrokeSerializers
    queryset = Stroke.objects.all()


class StrokeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticatedOrReadOnly,
    )
    model = Stroke
    serializer_class = StrokeSerializers
    queryset = Stroke.objects.all()
