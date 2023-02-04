from django.db import models
from django.contrib.auth import get_user_model
class Stroke(models.Model):

    G1 = "Male"
    G2 = "Female"
    R1 = "True"
    R2 = "False"
    M1 = "True"
    M2 = "False"
    W1 = "govt_job"
    W2 = "never_worked"
    W3 = "private"
    W4 = "self-employed"
    W5 = "children"
    S1 = "unknown"
    S2 = "formerly_smoked"
    S3 = "never_smoked"
    S4 = "smokes"
    H1 = "True"
    H2 = "False"
    D1 = "True"
    D2 = "False"

    GENDER = [
        (G1, "Male"),
        (G2, "Female"),
    ]
    RESIDENCE = [
        (R1, "True"),
        (R2, "False"),
    ]
    MARRIED = [
        (M1, "True"),
        (M2, "False"),
    ]
    WORK = [
        (W1, "govt_job"),
        (W2, "never_worked"),
        (W3, "private"),
        (W4, "Self-employed"),
        (W4, "children"),
    ]
    SMOKE = [
        (S1, "unknown"),
        (S2, "formerly_smoked"),
        (S3, "never_smoked"),
        (S4, "smokes"),
    ]
    HYPERTENSION = [
        (H1, "True"),
        (H2, "False"),
    ]
    HEART = [
        (D1, "True"),
        (D2, "False"),
    ]
    owner=models.ForeignKey(get_user_model(),models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=55, default=None, null=True)
    email = models.CharField(max_length=55, default=None, null=True)
    mobile = models.IntegerField(default=None, null=True)
    age = models.IntegerField(default=None, null=True)
    bmi = models.FloatField(default=None, null=True)
    avg_glucose_level = models.FloatField(default=None, null=True)

    gender = models.CharField(max_length=6, choices=GENDER, default=G1, null=True)
    residence_type = models.CharField(
        max_length=5, choices=RESIDENCE, default=R1, null=True
    )
    ever_married = models.CharField(
        max_length=5, choices=MARRIED, default=M1, null=True
    )
    work_type = models.CharField(max_length=32, choices=WORK, default=W2, null=True)
    smoking_status = models.CharField(
        max_length=32, choices=SMOKE, default=S1, null=True
    )
    hypertension = models.CharField(
        max_length=5, choices=HYPERTENSION, default=H1, null=True
    )
    heart_disease = models.CharField(max_length=5, choices=HEART, default=D1, null=True)
    status = models.CharField(max_length=8, null=True)
    def __str__(self):
        return self.name