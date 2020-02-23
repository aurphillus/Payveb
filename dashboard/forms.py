from django import forms
from .models import dealerinfo

class DealerInfo(forms.ModelForm):
    class Meta:
        model = dealerinfo
        fields = '__all__'
        widgets = {
            'organization_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_category': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gst_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'personal_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'organization_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control','rows': 5}),
            }
