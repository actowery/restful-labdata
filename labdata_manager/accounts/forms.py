from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# custom users will be essentially customers since employees will not be created with a public form
# leaving it vague for the future, perhaps other user types (suppliers, etc) may come about

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
          "username",
          "email",
          "payment_method",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
          "username",
          "email",
          "payment_method",
        )