from django import forms
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        # fields=('name','student','address')
        fields ="__all__"
        
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'student': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),

                    }