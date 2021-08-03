from django.contrib.auth.models import AbstractUser
from django.db import models
from django_pgviews import view as pg


    
class Project(models.Model):
    category_choices=(
    ('Web Ticketing','Web Ticketing'),
    ('Appointment','Appointment'),
    ('Queue Management','Queue Management'),
    ('Watsapp Ticketing','Watsapp Ticketing')
    )
    region_choices=(
    ('North America','North America'),
    ('South America','South America'),
    ('Europe','Europe'),
    ('Middle East','Middle East'),
    ('Africa','Africa'),
    ('Asia','Asia')
    )
    projectname= models.CharField(max_length=200, null=True)
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    sod=models.IntegerField()
    region=models.CharField(choices=region_choices, max_length=200)
    startdate=models.DateField()
    enddate=models.DateField()
    cost=models.IntegerField()
    webticket=models.BooleanField(null=True)
    appointment=models.BooleanField(null=True)
    watsapp=models.BooleanField(null=True)
    queue=models.BooleanField(null=True)
    count=models.IntegerField(null=True)
    modules=models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "projects"



   




