from django.db import models
from django.utils import timezone


class Form(models.Model):
    chategory_choice = (('EL','ELECTRONICS'),
                        ('FB','FASHION & BEAUTY'),
                        ('FO','FOOD & BEVERAGE'),
                        ('CD','CONSOMOTICS & DETERGENT'),
                        ('OT','OTHER'))
    type_choice = (('M','MANUFUCTURING'),
                   ('R','RETAIL'))
    companiesOwnerName = models.CharField(max_length = 225)
    companieName = models.CharField(max_length = 255)
    companieTypeChategory = models.CharField(max_length = 1,choices = type_choice)
    phone_name = models.CharField(max_length = 255)
    companieAdress = models.CharField(max_length = 255)
    chategory = models.CharField(max_length = 2,choices = chategory_choice,null = True,blank = True)
    custom_category = models.CharField(max_length = 225,null = True,blank = True)
    date = models.DateTimeField(default = timezone.now)
