from django.forms import ModelForm, forms
from .models import Messages


class MessForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_field'
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Your name'
            elif field_name == 'email':
                field.widget.attrs['placeholder'] = 'Your e-mail'
            elif field_name == 'text':
                field.widget.attrs['placeholder'] = 'Print a message'

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError(f"Type only the letters \"{name}\"")

        return name
