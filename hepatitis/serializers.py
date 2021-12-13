from rest_framework import serializers
from .models import Hepatitis


class HepatitisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hepatitis
        fields = "__all__"
