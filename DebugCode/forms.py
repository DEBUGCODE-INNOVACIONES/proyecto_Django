from django import forms

class ContactForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
