from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        #toLower
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email' ]

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Profile img"
    class Meta:
        model = Profile
        fields = ['img']
