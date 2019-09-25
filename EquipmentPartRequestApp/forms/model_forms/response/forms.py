from django.forms import ModelForm
from ....models.response.models import ResponseModel


class ResponseModelForm(ModelForm):
    class Meta:
        model = ResponseModel
        fields = ['comment']
