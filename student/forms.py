from django import forms

from .models import Submit


class SubmissionForm(forms.ModelForm):
    course = forms.CharField(label="Course")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
        self.fields["course"].widget.attrs["readonly"] = True

    class Meta:
        model = Submit
        fields = "__all__"
        exclude = ["feedback", "checked", "student"]
        widgets = {
            "work": forms.TextInput(attrs={"readonly": "readonly"}),
        }

    field_order = ["work", "course"]
