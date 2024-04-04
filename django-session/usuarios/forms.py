from django.contrib.auth import forms
from .models import Users

# Reescrevendo o model User padrão do Django para Users
# Estudar melhor sobre UserChangeForm e UserCreationForm

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users