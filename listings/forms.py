from django import forms
from .models import Listing, Job, Company

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__" 

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__" 

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__" 
