from django.db import models

# Create your models here.


class Visitor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'X'
    GENDER_OPTIONS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]
    dtRegistered = models.DateTimeField(auto_now_add=True)
    strFullName = models.CharField(max_length=256, blank=False)
    eGender = models.CharField(max_length=2,
                               choices=GENDER_OPTIONS,
                               default=OTHER)  # SELECT M, F, OR X
    dtBirth = models.DateField(max_length=8, 
                               auto_now=False, 
                               auto_now_add=False) # YYYY-MM-DD FORMAT
    strGovtIdNo = models.CharField(max_length=16, blank=False)
    strAddress = models.TextField(default='Indonesia')

    class Meta:
        ordering = ['dtRegistered']