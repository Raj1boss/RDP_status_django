from .models import user_rdp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RDPRegistration(forms.ModelForm):
    class Meta:
        model=user_rdp
        fields=['Emp_Id','IP_Address','Username','Password','Status']
        widgets={
            'Emp_Id' : forms.TextInput(attrs={'class':'form-control'}),
            'IP_Address': forms.TextInput(attrs={'class':'form-control'}),
            "Username":forms.TextInput(attrs={'class':'form-control'}),
            "Password":forms.TextInput(attrs={'class':'form-control'}),
            "Status":forms.TextInput(attrs={'class':'form-control'})
            }
        
        


    
    
            
            
      
        

