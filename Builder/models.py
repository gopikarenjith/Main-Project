from django.db import models
from Admin.models import*
from User.models import*
from Guest.models import*


class tbl_worker(models.Model):
    worker_name=models.CharField(max_length=50)
    worker_email=models.CharField(max_length=50)
    worker_contact=models.CharField(max_length=50)
    worker_photo=models.FileField(upload_to="Assets/WorkerDocs/")
    worker_password=models.CharField(max_length=50)
    worker_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    builder=models.ForeignKey(tbl_builders,on_delete=models.CASCADE)
    workertype=models.ForeignKey(tbl_workertype,on_delete=models.CASCADE)
class tbl_work(models.Model):
    work_title=models.CharField(max_length=50)
    work_details=models.CharField(max_length=50)
    work_photo=models.FileField(upload_to="Assets/WorkDocs/")
    work_date=models.DateField(auto_now_add=True)
    builder=models.ForeignKey(tbl_builders,on_delete=models.CASCADE)
class tbl_workgallery(models.Model):
    work_file=models.CharField(max_length=50)
    work=models.ForeignKey(tbl_work,on_delete=models.CASCADE)
class tbl_assign(models.Model):
    request=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
    worker=models.ForeignKey(tbl_worker,on_delete=models.CASCADE)
    assign_date=models.DateField(auto_now_add=True)
    assign_status=models.IntegerField(default=0)
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    builder=models.ForeignKey(tbl_builders,on_delete=models.CASCADE,null=True)
    worker=models.ForeignKey(tbl_worker,on_delete=models.CASCADE,null=True)



