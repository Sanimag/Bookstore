from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class USERForm(UserCreationForm):

    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'userImg', 'age', 'gender', 'info')


class USERChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('email', 'username', 'userImg', 'age', 'gender', 'info')
