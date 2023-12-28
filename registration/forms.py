from django import forms
from .models import Order,Department,Course,Material

class DateInput(forms.DateInput):
    input_type = 'date'
class OrderForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    purpose_choices = [
        ('Enquiry', 'Enquiry'),
        ('Place Order', 'Place Order'),
        ('Return', 'Return'),
        ('Help','Help'),
    ]
    purpose = forms.ChoiceField(choices=purpose_choices)
    materials_provide = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
                                                       widget=forms.CheckboxSelectMultiple)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model=Order
        fields=['name','dob','age','gender','phone_number','email','address','department','course','purpose','materials_provide']


        widgets = {
            'dob': DateInput(),
        }