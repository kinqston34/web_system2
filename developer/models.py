from django.db import models
from HRM.models import Staff
# Create your models here.

class Developer(models.Model):
    """
    IT工程師資料表

    欄位: 
    dev_id : IT 員工編號 , max=40 , pk (string)
    password : 密碼, max=20(string)
    
    """

    dev_id = models.ForeignKey(Staff,on_delete = models.CASCADE ,primary_key = True, limit_choices_to = {"departments":"IT"},db_column = "dev_id",related_name = "dev_id")
    password = models.CharField(max_length = 20,null=False)

    def save(self,*args, **kwargs):

        try:
            Staff.objects.get(staff_id = self.dev_id.staff_id , departments = "IT")
        except Staff.DoesNotExist:
            print("IT 找不到,不儲存")
            return False
        else:
            super().save(*args,**kwargs)
            return True

    class Meta:
        db_table = "developer"
