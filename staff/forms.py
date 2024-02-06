from django import forms
from .models import Borrowing,libraryBook

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['book', 'borrowed_person']
        labels = {
            'borrowed_person': 'Borrowed Person',
        }
        required = {
            'borrowed_person': True,
        }
    
    def __init__(self, *args, **kwargs):
        book_id = kwargs.pop('book_id', None)
        super().__init__(*args, **kwargs)
        
        if book_id:
            self.fields['book'].initial = book_id
            self.fields['book'].widget = forms.HiddenInput()
            self.fields['book'].disabled = True
        self.fields['borrowed_person'].widget.attrs.update({'class': 'form-control'})
    def clean_book(self):
        book_id = self.cleaned_data['book']
        return book_id
class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = libraryBook
        fields = ['name', 'author']
        labels = {
            'name': 'Name',
            'author': 'Author',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }