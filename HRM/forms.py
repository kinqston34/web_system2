from django import forms

class StaffForm(forms.Form):

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
    on_the_job = forms.BooleanField(required=False)

class HRForm(forms.Form):
    
    """
    model: HR 

    columns: 
    hr_id, password: (string)
    manager : (bool) required=False 
    """
    
    hr_id = forms.CharField(max_length=8)
    password = forms.CharField(max_length=20)
    manager = forms.BooleanField(required=False)