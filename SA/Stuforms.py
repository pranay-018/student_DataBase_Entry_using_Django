from django import forms
class stuforms(forms.Form):
    name=forms.CharField(max_length=30)
    regno=forms.IntegerField()
    m1=forms.FloatField()
    m2=forms.FloatField()
class srcform(forms.Form):
    s_name=forms.CharField(max_length=30) 
class delform(forms.Form):
    d_name=forms.CharField(max_length=30)
class upform(forms.Form):
    u_name=forms.CharField(max_length=30)           