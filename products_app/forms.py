from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'placeholder': 'Search products...',
            'style': 'width: 300px'
        })
    ) 