from rest_framework import serializers
from .models import Stroke


class StrokeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stroke
        fields = "__all__"
