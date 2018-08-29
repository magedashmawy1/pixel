# make sure this is at the top if it isn't already
from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required= True)
    contact_mobile = forms.CharField(required=True, max_length=11)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label ="Name"
        self.fields['contact_email'].label ="Email"
        self.fields['contact_mobile'].label ="Mobile"
        self.fields['content'].label = "Your Message"
