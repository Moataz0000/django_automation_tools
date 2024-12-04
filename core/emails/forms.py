from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_list', 'subject', 'body', 'attachment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('email_list', css_class='form-control'),
            Field('subject', css_class='form-control'),
            Field('body', css_class='form-control'),
            Field('attachment', css_class='form-control'),
            Submit('submit', 'Send Email', css_class='btn btn-primary')
        )
