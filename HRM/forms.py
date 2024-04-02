from django import forms
from HRM.models import HR
from django.core.exceptions import ValidationError

class StaffForm(forms.Form):     # 建立員工資料表用的Form

    """
    model: Staff 

    columns: 
    staff_id, name, en_name, departments, level: (string)
    on_the_job : (bool) required=False 
    """

    staff_id = forms.CharField(max_length=8)
    name = forms.CharField(max_length=20)
    en_name = forms.CharField(max_length=20)
    departments = forms.CharField(max_length=5)
    level = forms.CharField(max_length=1)
    # on_the_job = forms.BooleanField(required=False)

class HRForm(forms.Form):   #HR 建立時用的Form
    
    """
    model: HR 

    columns: 
    hr_id, password: (string)
    
    """
    
    hr_id = forms.CharField(max_length=8)
    password = forms.CharField(max_length=20)
   

class HRMLoginForm(HRForm):    #登入用Form

    def clean(self):

        hr_id = self.cleaned_data.get("hr_id")
        password = self.cleaned_data.get("password")
        
        try:
            HR.objects.get(hr_id = hr_id,password = password)
        except HR.DoesNotExist:
            raise ValidationError("db no query")  #新增驗證錯誤到 forms.error中
        else:
            return self.cleaned_data
        
    

        



