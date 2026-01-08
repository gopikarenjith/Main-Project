from django.db import models
from Admin.models import*


# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    # user_gender=models.CharField(max_length=50)
    # user_dob=models.DateField()
    user_password=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to="Assets/UserDocs/")
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
class tbl_builders(models.Model):
    builders_name=models.CharField(max_length=50)
    builders_email=models.CharField(max_length=50)
    builders_contact=models.CharField(max_length=50)
    builders_address=models.CharField(max_length=50)
    builders_logo=models.FileField(upload_to="Assets/BuilderDocs/")
    builders_license=models.FileField(upload_to="Assets/BuilderDocs/")
    builders_status=models.IntegerField(default=0)
    builders_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    builders_doj=models.DateField(auto_now_add=True)
