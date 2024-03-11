from django.db import models

# Create your models here.

class Staff(models.Model):
    """
    員工資料表:

    欄位:
    * staff_id: 員工id , string , max=8 ,pk
    * name: 員工姓名 , string , max=20
    * en_name: 員工英文名子 , string , max=20
    * departments : 部門代號 
        Chair: 董事長
        Pres: 總經理
        HR: 人事部
        IT: 資訊部
        ED: 工程部
    * level: 主管(M) or 一般員工(S)
    * on_the_job: 在職狀態(在職:True,離職:False) , boolean
    """
    
    staff_id = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=20,null=False)  
    en_name = models.CharField(max_length=20,null=False) 
    departments = models.CharField(max_length=5,null=False)
    level = models.CharField(max_length=1,null=False)
    on_the_job = models.BooleanField(default=True) 

    class Meta:
        db_table="staff"

class HR(models.Model):

    """
    人事系統資料表:

    欄位:
    * hr_id : HR員工編號 , string , max=8 , pk
    * password: 密碼 , string , max=20
    * manager: 主管 , boolen , 預設False
    """

    hr_id = models.CharField(max_length=8,primary_key=True)
    password = models.CharField(max_length=20,null=False)
    manager = models.BooleanField(default=False)

    class Meta:
        db_table = "HR"




