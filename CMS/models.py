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

class MaterialSupply(models.Model):
    '''
    原料供應商資料表
    supplier_id : pk,max=7
    name : max=40
    address : max=50
    tel : max=9
    salesman : max=10 
    salesman_phone : max=10

    '''
    supplier_id = models.CharField(max_length=7,primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=9)
    salesman = models.CharField(max_length=10)
    salesman_phone = models.CharField(max_length=10)

    class Meta():
        db_table = "Material_Supply"

class RawMaterial(models.Model):

    '''
    原料資料表
    material_id : pk,max=8
    name : max=30
    category : max=2 
    supplier_id : fk , MaterialSupply
    '''
    material_id = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=2)
    supplier_id = models.ForeignKey(MaterialSupply,on_delete=models.CASCADE,db_column="supplier_id",related_name="material_supplies")

    class Meta():
        db_table = "Raw_Material"





















