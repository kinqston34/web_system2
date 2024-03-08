from django import forms

class DeveloperLoginForm(forms.Form):

    account = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    # name = forms.CharField(max_length=20)
    # manager = forms.BooleanField()

class DeveloperCreateForm(forms.Form):

    dev_id = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    manager = forms.BooleanField(required=False)



