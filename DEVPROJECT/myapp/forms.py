from django import forms  
from myapp.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['Codigoproduto', 'Nome', 'Codigobarras','Preco'] 
        widgets = { 'Codigoproduto': forms.NumberInput(attrs={ 'class': 'form-control' }), 
            'Nome': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Codigobarras': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'Preco': forms.NumberInput (attrs={ 'class': 'form-control' }),
      }
        