from django import forms

from .models.models import Comment, Order
from .models.assays import assay_list
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")

class OrderForm(forms.ModelForm):
    company = forms.CharField(max_length=100)
    assays = forms.ChoiceField(choices=assay_list())

    class Meta:
        model = Order
        fields = ("company", "assays")

