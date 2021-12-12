from rest_framework import serializers
from .models import Stroke


class StrokeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stroke
        fields = (
            "name",
            "email",
            "mobile",
            "age",
            "bmi",
            "avg_glucose_level",
            "gender",
            "residence_type",
            "ever_married",
            "work_type",
            "smoking_status",
            "hypertension",
            "heart_disease",
            "status"
        )
