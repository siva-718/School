from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['name','dob','age','gender','phone_number','email','address','department','course','purpose','materials_provide']