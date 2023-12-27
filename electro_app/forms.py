from django import forms
from electro_app.models import customer_request,review,subscriber
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class reg_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
         
class booking_form(forms.ModelForm):
    class Meta:
        model=customer_request
        fields=['customer_name','email_ID','phone_number','address','city','state','pin_code','request_Type','description','date']
         
class review_form(forms.ModelForm):
    class Meta:
        model=review
        fields=['review_message']

class sub_form(forms.ModelForm):
    class Meta:
        model=subscriber
        fields=['email_ID']
                  