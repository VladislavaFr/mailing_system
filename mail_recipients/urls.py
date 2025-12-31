from django.urls import path
from mail_recipients.views import (
    MailRecipientCreateView,
    MailRecipientListView,
    MailRecipientDetailView,
    MailRecipientUpdateView,
    MailRecipientDeleteView,
)

app_name = "mail_recipients"

urlpatterns = [
    path("create/", MailRecipientCreateView.as_view(), name="create_mail_recipient"),
    path("list/", MailRecipientListView.as_view(), name="list_mail_recipient"),
    path("<int:pk>/", MailRecipientDetailView.as_view(), name="detail_mail_recipient"),
    path("<int:pk>/update/", MailRecipientUpdateView.as_view(), name="update_mail_recipient"),
    path("<int:pk>/delete/", MailRecipientDeleteView.as_view(), name="delete_mail_recipient"),
]