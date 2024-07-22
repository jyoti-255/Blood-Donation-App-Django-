from django import forms
class BdForm(forms.Form):
      name=forms.CharField(required=False)
      age=forms.IntegerField(required=False)
      weight=forms.FloatField(required=False)