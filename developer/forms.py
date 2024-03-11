from django import forms

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

class DeveloperCreateForm(forms.Form):

    """
    model: Developer 

    columns: 
    dev_id, password: (string)
    manager : (bool) required=False 
    """
    dev_id = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    manager = forms.BooleanField(required=False)



