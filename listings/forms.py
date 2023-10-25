
from django import forms
from .models import Merchant
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)
   is_active = forms.BooleanField()
   
class MerchantForm(forms.ModelForm):
   class Meta:
      model=Merchant
      fields='__all__'