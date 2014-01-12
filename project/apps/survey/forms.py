from django.forms import ModelForm, ValidationError
from .models import HealthStateSequenceUpload, SurveyResponse, HealthStateRating, SurveyConfig


class HealthStateSequenceUploadForm(ModelForm):
    class Meta:
        model = HealthStateSequenceUpload

class SurveyConfigForm(ModelForm):
    class Meta:
        model = SurveyConfig

class DemographicForm(ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ("age", "education", "household_income", "diagnosed_with_serious_mental_illness",
            "diagnosed_with_schizophrenia", "diagnosed_with_depression", "diagnosed_with_bipolar",
            "diagnosed_with_other", "diagnosed_with_dont_know", "family_diagnosed_with_serious_mental_illness",
            "family_diagnosed_with_schizophrenia", "family_diagnosed_with_depression",
            "family_diagnosed_with_bipolar", "family_diagnosed_with_other", "family_diagnosed_with_dont_know",
        )

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 0 or data > 130:
            raise ValidationError("Please enter a valid age.")
        return data


class VASForm(ModelForm):
    class Meta:
        model = HealthStateRating
        fields = ("vas_rating",)

    def clean_vas_rating(self):
        data = self.cleaned_data['vas_rating']
        if data is None:
            raise ValidationError("This field is required.")
        return data


class TTOForm(ModelForm):
    class Meta:
        model = HealthStateRating
        fields = ("tto_rating",)

    def clean_tto_rating(self):
        data = self.cleaned_data['tto_rating']
        if data is None:
            raise ValidationError("This field is required.")
        return data
