from django import forms
from .models import Borrowing, libraryBook,Alert,Fee,Payment


class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ["book", "borrowed_person"]
        labels = {
            "borrowed_person": "Borrowed Person",
        }
        required = {
            "borrowed_person": True,
        }

    def __init__(self, *args, **kwargs):
        book_id = kwargs.pop("book_id", None)
        super().__init__(*args, **kwargs)

        if book_id:
            self.fields["book"].initial = book_id
            self.fields["book"].widget = forms.HiddenInput()
            self.fields["book"].disabled = True
        self.fields["borrowed_person"].widget.attrs.update({"class": "form-control"})

    def clean_book(self):
        book_id = self.cleaned_data["book"]
        return book_id


class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = libraryBook
        fields = ["name", "author"]
        labels = {
            "name": "Name",
            "author": "Author",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
        }
class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'
        widgets = {
            'route': forms.Select(attrs={'class': 'form-control'}),
            'alert_type': forms.Select(attrs={'class': 'form-control'}),
            'alert_message': forms.Textarea(attrs={'class': 'form-control'}),
            'alert_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
#college_fee_form
class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = '__all__'
        widgets = {
            'fee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'fee': forms.Select(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }