from django import forms

from .models.models import Comment, Order
from common.constants import AVAILABLE_ASSAYS
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ("company", "assays", "quantity")
        widgets = {
                    "assays": forms.Select(choices=AVAILABLE_ASSAYS),
                    "company": forms.TextInput(),
                    "quantity": forms.NumberInput(),
                }
