from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label_suffix='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type message here'}), required=True)
    field_order = ['email', 'name', 'subject', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email
