from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['additional_info', 'avatar']  # Agrega aquí los campos que quieras incluir en el formulario
