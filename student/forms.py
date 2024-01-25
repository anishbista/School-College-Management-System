from django import forms

from .models import Submit


class SubmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Submit
        fields = "__all__"
        exclude = ["feedback", "checked"]
        widgets = {
            "work": forms.TextInput(attrs={"readonly": "readonly"}),
            "student": forms.TextInput(attrs={"readonly": "readonly"}),
        }
