from django import forms
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from .models import Comment, Order, Assay, OrderAssay
from common.constants import AVAILABLE_ASSAYS, STATUS_OPTIONS, RESTULT_OPTIONS

        
class OrderAssayForm(forms.ModelForm):
    class Meta:
        model = OrderAssay
        fields = ('assay', 'quantity')


class OAFormSet(BaseInlineFormSet):
    def clean(self):
        # Override the clean method to remove duplicate assay data validation
        pass

OrderAssayFormSet = inlineformset_factory(
    Order,
    OrderAssay,
    form=OrderAssayForm,
    formset=OAFormSet,
    extra=1,  # Number of additional forms to display
    can_delete=True,  # Allow deletion of existing forms
)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")

class OrderForm(forms.ModelForm):

    orderassays = OrderAssayFormSet

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.orderassays = OrderAssayFormSet(instance=self.instance)
        else:
            self.orderassays = OrderAssayFormSet()
    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        for form in self.orderassays:
            orderassay = form.save(commit=False)
            orderassay.order = instance
            orderassay.save()
        return instance

    class Meta:
        model = Order
        fields = ("company",)
        widgets = {
                    "company": forms.TextInput(),
                }

