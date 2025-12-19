from django.db import models
from Guest.models import*

# Create your models here.
class tbl_complaint(models.Model):
       Complaint_title=models.CharField(max_length=50)
       Complaint_content=models.CharField(max_length=50)
       Complaint_date=models.DateField(auto_now_add=True)
       Complaint_reply=models.CharField(max_length=50,null=True)
       Complaint_status=models.IntegerField(default=0)
       user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
class tbl_request(models.Model):
       request_content=models.CharField(max_length=50)
       request_file=models.FileField(upload_to="Assets/requestDocs/")
       request_date=models.DateField(auto_now_add=True)
       request_status=models.IntegerField(default=0)
       request_amount=models.CharField(max_length=50,null=True)
       user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
       builder=models.ForeignKey(tbl_builders,on_delete=models.CASCADE)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    builder=models.ForeignKey(tbl_builders,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)