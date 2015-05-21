from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from principal.models import Editorial, Persona

__author__ = 'Ruben'

class AddNewsForm(forms.Form):
    titulo = forms.CharField(max_length=128)
    cuerpo = forms.CharField(widget=forms.Textarea)
    publicadorId = forms.ModelChoiceField(queryset=Persona.objects.all(), to_field_name="id", label= 'Selecciona persona')
    editorialId = forms.ModelChoiceField(queryset=Editorial.objects.all(), to_field_name="id", label= 'Selecciona editorial')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_action = 'save'
    helper.label_class = "col-sm-2"
    helper.field_class = "col-sm-10"
    helper.layout = Layout(
        Field('titulo', css_class="input-sm"),
        Field('cuerpo', css_class="input-sm"),
        Field('publicadorId', css_class="input-sm"),
        Field('editorialId', css_class="input-sm"),
        FormActions(Submit('save', 'Enviar', css_class='btn-primary'))
    )
