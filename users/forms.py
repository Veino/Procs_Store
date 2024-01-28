from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ProcsUser


class ProcsUserCreationForm(UserCreationForm):

    class Meta:
        model = ProcsUser
        fields = ("email",)


class ProcsUserChangeForm(UserChangeForm):

    class Meta:
        model = ProcsUser
        fields = ("email",)