from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Hepatitis(models.Model):

    G1 = "Male"
    G2 = "Female"
    Steriod1 = "True"
    Steriod2 = "False"
    Antivirals1 = "True"
    Antivirals2 = "False"
    Fatique1 = "True"
    Fatique2 = "False"
    Malaise1 = "True"
    Malaise2 = "False"
    Anorexia1 = "True"
    Anorexia2 = "False"
    Liver_big1 = "True"
    Liver_big2 = "False"
    Liver_firm1 = "True"
    Liver_firm2 = "False"
    Spleen_pallpable1 = "True"
    Spleen_pallpable2 = "False"
    Spidres1 = "True"
    Spiders2 = "False"
    Ascites1 = "True"
    Ascites2 = "False"
    Varices1 = "True"
    Varices2 = "False"
    Histology1 = "True"
    Histology2 = "False"

    GENDER = [
        (G1, "Male"),
        (G2, "Female"),
    ]
    STERIOD=[
        (Steriod1, "True"),
        (Steriod2, "False")
    ]
    ANTIVIRALS = [
        (Antivirals1, "True"),
        (Antivirals2, "False")
    ]
    FATIQUE=[
        (Fatique1, "True"),
        (Fatique2, "False")
    ]
    MALAISE= [
        (Malaise1, "True"),
        (Malaise2, "False")       
    ]
    ANOREXIA = [
        (Anorexia1, "True"),
        (Anorexia2, "False")          
    ]
    LIVER_BIG = [
        (Liver_big1, "True"),
        (Liver_big2, "False")         
    ]
    LIVER_FIRM = [
        (Liver_firm1, "True"),
        (Liver_firm2, "False")         
    ]
    SPLEEN_PALLPABLE=[
        (Spleen_pallpable1, "True"),
        (Spleen_pallpable2, "False")       
    ]
    SPIDERS = [
        (Spidres1, "True"),
        (Spiders2, "False")      
    ]
    ASCITES = [
        (Ascites1, "True"),
        (Ascites2, "False")          
    ]
    VARICES = [
        (Varices1, "True"),
        (Varices2, "False")  
    ]
    HISTOLOGY = [
        (Histology1, "True"),
        (Histology2, "False")    
    ]

    owner=models.ForeignKey(get_user_model(),models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=55, default=None, null=True)
    email = models.CharField(max_length=55, default=None, null=True)
    mobile = models.IntegerField(default=None, null=True)
    age = models.IntegerField(default=None, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default=G1, null=True)
    steroid = models.CharField(max_length=6, choices=STERIOD, default=Steriod2, null=True)
    antivirals = models.CharField(max_length=6, choices=ANTIVIRALS, default=Antivirals2, null=True)
    fatigue = models.CharField(max_length=6, choices=FATIQUE, default=Fatique2, null=True)
    malaise = models.CharField(max_length=6, choices=MALAISE, default=Malaise2, null=True)
    anorexia = models.CharField(max_length=6, choices=ANOREXIA, default=Anorexia2, null=True)
    liver_big = models.CharField(max_length=6, choices=LIVER_BIG, default=Liver_big2, null=True)
    liver_firm = models.CharField(max_length=6, choices=LIVER_FIRM, default=Liver_firm2, null=True)
    spleen_palpable = models.CharField(max_length=6, choices=SPLEEN_PALLPABLE, default=Spleen_pallpable2, null=True)
    spiders = models.CharField(max_length=6, choices=SPIDERS, default=Spiders2, null=True)
    ascites = models.CharField(max_length=6, choices=ASCITES, default=Ascites2, null=True)
    varices = models.CharField(max_length=6, choices=VARICES, default=Varices2, null=True)
    bilirubin = models.FloatField(default=None, null=True)
    alk_phosphate = models.FloatField(default=None, null=True)
    sgot = models.FloatField(default=None, null=True)
    albumin = models.FloatField(default=None, null=True)
    protime = models.FloatField(default=None, null=True)
    histology = models.CharField(max_length=6, choices=HISTOLOGY, default=Histology2, null=True)


    def __str__(self):
        return self.name