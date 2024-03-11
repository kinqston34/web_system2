from django.db import models

# Create your models here.

class Developer(models.Model):
    """
    IT工程師資料表

    欄位: 
    dev_id : IT 員工編號 , max=40 , pk (string)
    password : 密碼, max=20(string)
    manager: manager: 主管, 預設False (boolen) 
    """

    dev_id = models.CharField(max_length = 40,primary_key=True)
    password = models.CharField(max_length = 20,null=False)
    manager = models.BooleanField(default=False)

    class Meta:
        db_table = "developer"
