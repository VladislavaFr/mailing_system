from django import forms
from mail_recipients.models import CustomMailRecipient


class MailRecipientForm(forms.ModelForm):
    class Meta:
        model = CustomMailRecipient
        fields = ["name", "email", "phone_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Имя клиента"})
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "email@example.com"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control", "placeholder": "222-22-22"})
