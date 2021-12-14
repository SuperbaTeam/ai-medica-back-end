from django.contrib.auth import get_user_model
from django.db import models


class Cancer(models.Model):

    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(default=None, null=True, max_length=55)
    email = models.CharField(max_length=55, default=None, null=True)
    age = models.IntegerField(default=None, null=True)
    texture_mean = models.FloatField(default=None, null=True)
    area_mean = models.FloatField(default=None, null=True)
    smoothness_mean = models.FloatField(default=None, null=True)
    compactness_mean = models.FloatField(default=None, null=True)
    concavity_mean = models.FloatField(default=None, null=True)
    concave_points_mean = models.FloatField(default=None, null=True)
    state = models.FloatField(default=None, null=True)

    def __str__(self):
        return self.name
