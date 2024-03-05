from django import forms
from .models import Volunteer,News,CustomUser, Contact
from django.contrib.auth.forms import UserCreationForm
from tinymce.widgets import TinyMCE


class VolunteerForm(forms.ModelForm):
   
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    full_name=forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    

    subject=forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'subject'}))
    cv=forms.FileField(label="CV upload",max_length=100, help_text={'YOUR HELP TEXT HERE'},widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'cv'}))
    comment=forms.CharField(label="",max_length=100, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment'}))
    class Meta:
        model=Volunteer
        fields=('full_name','email','subject','cv','comment')

        help_texts = {
             'cv': 'YOUR HELP TEXT HERE',
        }
        widgets = {
            'cv' : forms.FileInput(attrs={'class': 'form-control'}),

        }

        # Widgets={
        #     'full_name':forms.TextInput(attrs={'class':'form-control','placeholder':'jackson'}),
        #     'email':forms.EmailField(label="email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
        # }
        # def __init__(self, *args, **kwargs):
        #     super(VolunteerForm, self).__init__(*args, **kwargs)

        #     self.fields['full_name'].widget.attrs['class']='form-control'
        #     self.fields['full_name'].widget.attrs['placeholder']='Username'
        #     self.fields['full_name'].label=''
        #     self.fields['full_name'].help_text='<span class= "form-text test-muted"> <small>Required. 150 or fewer letters digits and @#/& only </small></span> '


class ContactForm(forms.ModelForm):
   
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email address'}))
    name=forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    

    message=forms.CharField(label="",max_length=100, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment'}))
    
    class Meta:
        model=Contact
        fields=('name','email','message')




class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=('photo','author','title','post')

class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")



class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class RegisterForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2','is_admin','is_member','is_users')
