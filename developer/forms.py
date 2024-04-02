from django import forms
from developer.models import Developer
from django.core.exceptions import ValidationError

class DeveloperLoginForm(forms.Form):

    """
    model: Developer 

    columns: 
    account -> dev_id(string)
    password -> password(string) 
    """

    account = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    # name = forms.CharField(max_length=20)
    # manager = forms.BooleanField()

    def clean(self):

        dev_id = self.cleaned_data.get("account")
        password = self.cleaned_data.get("password")
        try:
            Developer.objects.get(dev_id = dev_id,password = password)
            
        except Developer.DoesNotExist:
            print("error")
            raise ValidationError("db no query")
        else:
            return self.cleaned_data

class DeveloperCreateForm(forms.Form):

    """
    model: Developer 

    columns: 
    dev_id, password: (string)
    """
    dev_id = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)


            






