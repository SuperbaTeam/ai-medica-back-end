from django.contrib.auth import get_user_model
from django.db import models


class Cancer(models.Model):

    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    texture_mean = models.FloatField(default=0)
    area_mean = models.FloatField(default=0)
    smoothness_mean = models.FloatField(default=0)
    compactness_mean = models.FloatField(default=0)
    concavity_mean = models.FloatField(default=0)
    concave_points_mean = models.FloatField(default=0)
    state = models.FloatField(default=0)

    def __str__(self):
        return self.owner
