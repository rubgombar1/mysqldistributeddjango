from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

__author__ = 'Ruben'

class AddPersonForm(forms.Form):
    nombre = forms.CharField(max_length=32)
    apellidos = forms.CharField(max_length=64)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_action = 'save'
    helper.label_class = "col-sm-2"
    helper.field_class = "col-sm-10"
    helper.layout = Layout(
        Field('nombre', css_class="input-sm"),
        Field('apellidos', css_class="input-sm"),
        FormActions(Submit('save', 'Enviar', css_class='btn-primary'))
    )
