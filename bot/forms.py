from django import forms

from bot.models import Profile, AdminPanel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'exeterenal_id',
            'username',
            'f_name',
            'l_name',
        )

        widgets = {
            'username': forms.TextInput,
        }



