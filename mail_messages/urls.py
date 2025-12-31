from django.urls import path
from mail_messages.views import (
    HomeView,
    EmailMessageCreateView,
    EmailMessageDetailView,
    EmailMessageListView,
    EmailMessageUpdateView,
    EmailMessageDeleteView,
    MailingCreateView,
    MailingListView,
    MailingDetailView,
    MailingUpdateView,
    MailingDeleteView,
)

app_name = "mail_messages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    # Email Messages
    path("email/create/", EmailMessageCreateView.as_view(), name="create_email"),
    path("email/<int:pk>/", EmailMessageDetailView.as_view(), name="detail_email"),
    path("email/list/", EmailMessageListView.as_view(), name="list_email"),
    path("email/<int:pk>/update/", EmailMessageUpdateView.as_view(), name="update_email"),
    path("email/<int:pk>/delete/", EmailMessageDeleteView.as_view(), name="delete_email"),

    # Mailings
    path("mailing/create/", MailingCreateView.as_view(), name="create_mailing"),
    path("mailing/list/", MailingListView.as_view(), name="list_mailing"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="detail_mailing"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="update_mailing"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="delete_mailing"),
]
