from django import forms
from lists.models import Item

EMPTY_ERROR_MESSAGE = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):
    def save(self, for_list):
        self.instance.list = for_list
        return super().save()

    class Meta:
        model = Item
        fields = ('text', )
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg'
            })
        }
        error_messages = {
            'text': {'required':EMPTY_ERROR_MESSAGE}
        }