from django.db import models
from datetime import date

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
    * hr_id : HR員工編號 , pk , fk => from Staff departments = HR
    * password: 密碼 , string , max=20
    """

    hr_id = models.ForeignKey(Staff,on_delete=models.CASCADE,primary_key=True,limit_choices_to={"departments":"HR"},db_column = "hr_id",related_name="hr_id")
    password = models.CharField(max_length=20,null=False)
    
    def save(self,*args, **kwargs):

        try:
            staff = Staff.objects.get(staff_id = self.hr_id.staff_id , departments = "HR")
        except Staff.DoesNotExist :
            print("HR找不到,不儲存")
            return False
        else:
            super().save(*args,**kwargs)
            return True

    class Meta:
        db_table = "HR"

class MealSupplier(models.Model):

    """
    餐點供應商資料表

    ms_id : 店家編號,int ,max=8 ,pk,Fk
    name : 店家名 ,string ,max=20 ,NOT NULL
    phone : 店家電話 ,string ,max=10 ,NOT NULL
    contact_person : 店家負責人 ,string ,max=10 ,NOT NULL
    contact_person_phone : 店家負責人電話 ,string ,max=10 ,NOT NULL
    meal_time : 早餐(B) 午餐(L) 晚餐(D) 下午茶(A) 宵夜(N) ,string ,max=5 ,NOT NULL  
    take_way : 自取(S) 外送(D) ,string ,max=2 ,NOT NULL 
    score : 評分 ,float ,一位小數
    """

    ms_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,null=False)
    phone = models.CharField(max_length=10,null=False)
    contact_person = models.CharField(max_length=10,null=False)
    contact_person_phone = models.CharField(max_length=10,null=False)
    meal_time = models.CharField(max_length=5,null=False)
    take_way = models.CharField(max_length=2,null=False)
    score = models.FloatField(null=False)

    class Meta:
        db_table = "meal_supplier"

class StaffAccount():

    """
    員工餘額資料表

    staff_id : 員工id , pk , FK(Staff)
    balance : 餘額 , int , max_digits=6,default=0
    time : 時間 , date, default=date.today
    """

    staff_id = models.OneToOneField(Staff,on_delete=models.CASCADE,primary_key=True)
    type = models.CharField(max_length=1,null=False)
    balance = models.IntegerField(default=0)
    time = models.DateField(default=date.today)

    class Meta:
        db_table = "staff_account"



