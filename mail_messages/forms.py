from django import forms
from mail_messages.models import CustomMessage, Mailing

class MailMessagesForm(forms.ModelForm):
    class Meta:
        model = CustomMessage
        fields = ["subject", "body"]

class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ["name", "description"]

class MailingModeratorForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ["name", "description", "is_moderated"]
