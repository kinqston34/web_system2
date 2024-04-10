from django import forms
from CMS.models import CMS
from django.core.exceptions import ValidationError

class CMSLoginForm(forms.Form):

    """
    model: CMS 

    columns: 
    account -> CMS_id(string)
    password -> password(string) 
    """

    account = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)

    def clean(self):

        CMS_id = self.cleaned_data.get("account")
        password = self.cleaned_data.get("password")
        try:
            CMS.objects.get(CMS_id = CMS_id,password = password)
            
        except CMS.DoesNotExist:
            print("error")
            raise ValidationError("db no query")
        else:
            return self.cleaned_data

class CMSCreateForm(forms.Form):    #建立用Form

    """
    model: Developer 

    columns: 
    CMS_id, password: (string)
    """
    CMS_id = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)