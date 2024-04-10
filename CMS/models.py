from django.db import models
from HRM.models import Staff
# Create your models here.

class CMS(models.Model):

    """
    後臺管理系統資料表

    CMS_id : pk,fk from Staff 
    password : char , max=20 , null=False
    """

    CMS_id = models.ForeignKey(Staff, on_delete=models.CASCADE,primary_key = True,limit_choices_to={"developments":"ED"},db_column="CMS_id",related_name="CMS_id")
    password = models.CharField(max_length = 20,null=False)

    def save(self,*args, **kwargs):

        try:
            Staff.objects.get(staff_id = self.CMS_id.staff_id , departments = "ED")
        except Staff.DoesNotExist:
            print("ED 找不到,不儲存")
            return False
        else:
            super().save(*args,**kwargs)
            return True

    class Meta():
        db_table = "CMS"