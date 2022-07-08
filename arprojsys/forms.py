from django.db.models import fields
from django.forms import ModelForm
from .models import HealthyContact, ModPayDate

class ContactForm(ModelForm):
    class Meta:
        model = HealthyContact
        fields = ['LName', 'Fname', 'PAddress', 'Pnumber', 'Food', 'Order']

class PayForm(ModelForm):
    class Meta:
        model = ModPayDate
        fields = ['DToday', 'DelToday', 'Mop']
 
