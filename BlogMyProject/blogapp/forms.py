from django import forms
from blogapp.models import Comments,Login
class EmailSendingForm(forms.Form):
    Email=forms.EmailField()


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')

class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
