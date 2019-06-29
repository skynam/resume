from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'form-control', 'placeholder': 'Enter name', 'title': 'Please enter your name (at least 2 characters)', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'Enter email', 'title': 'Please enter a valid email address', 'required': True}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': '3', 'rows': '5',
                                                            'placeholder': 'Enter your message...', 'title': 'Please enter your message (at least 10 characters)', 'required': False}))
