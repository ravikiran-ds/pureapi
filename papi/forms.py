from .models import StuData
from django import forms

class StuForm(forms.ModelForm):
    class Meta:
        model=StuData
        fields=["name","score","type"]

    def clean(self,*args,**kwargs):
        data=self.cleaned_data
        f=["name","score","type"]
        for i in f:
            var1=data.get(i,None)
            if var1=='' or var1==None:
                raise forms.ValidationError("Name Cannot be empty")
                return False
                break
            else:
                return super().clean(*args,**kwargs)
