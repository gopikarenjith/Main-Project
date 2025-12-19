from django.db import models
from Builder.models import*

# Create your models here.
class tbl_updates(models.Model):
    updates_content=models.CharField(max_length=50)
    assign=models.ForeignKey(tbl_assign,on_delete=models.CASCADE)
    updates_date=models.DateField(auto_now_add=True)
    updates_status=models.IntegerField(default=0)