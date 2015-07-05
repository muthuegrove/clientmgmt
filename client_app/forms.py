from django import forms
from django.contrib.auth.models import User


class ClientCreationForm(forms.Form):
    '''
    Client creation form
    '''
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    company_info = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':45}))

    def clean_name(self):
        name = self.cleaned_data['name'].strip()       
        try:
            user=User.objects.get(username__iexact=name)
        except User.DoesNotExist:
            return name
        raise forms.ValidationError(u'This name is already exist. Please choose another')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            user=User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'This email ID is already exist. Please choose another')