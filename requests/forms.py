 
from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'title...'
        }
    ))
    issue = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your request...'
        }
    ))
    
    class Meta:
        model = Request
        fields = ('title','issue')


class RequestEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Request
        fields = ('is_closed',)

class RequestSuperUserForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('employee','is_closed')