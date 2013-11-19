from django.forms import ModelForm
from .models import HealthStateSequenceUpload


class HealthStateSequenceUploadForm(ModelForm):
    class Meta:
        model = HealthStateSequenceUpload
