from django import forms
from app.models import *

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    



class FriendshipList(forms.ModelForm):
    class Meta:
        model=FriendList
        fields='__all__'
