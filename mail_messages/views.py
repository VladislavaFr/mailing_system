from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from mail_messages.models import CustomMessage, Mailing
from mail_messages.forms import MailMessagesForm, MailingForm, MailingModeratorForm

class HomeView(TemplateView):
    template_name = "mail_messages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['messages_count'] = CustomMessage.objects.filter(owner=user).count()
            context['mailing_stats'] = Mailing.get_user_stats(user)
        return context


# --- Messages Views ---
class EmailMessageCreateView(LoginRequiredMixin, CreateView):
    model = CustomMessage
    form_class = MailMessagesForm
    template_name = "mail_messages/create_email.html"
    success_url = reverse_lazy("mail_messages:list_email")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EmailMessageDetailView(LoginRequiredMixin, DetailView):
    model = CustomMessage
    template_name = "mail_messages/detail_email.html"


class EmailMessageListView(LoginRequiredMixin, ListView):
    model = CustomMessage
    template_name = "mail_messages/list_email.html"
    context_object_name = "objects_list"

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Moderator").exists():
            return CustomMessage.objects.all()
        return CustomMessage.objects.filter(owner=user)


class EmailMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomMessage
    form_class = MailMessagesForm
    template_name = "mail_messages/update_email.html"
    success_url = reverse_lazy("mail_messages:list_email")


class EmailMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomMessage
    template_name = "mail_messages/confirm_delete_message.html"
    success_url = reverse_lazy("mail_messages:list_email")


# --- Mailings Views ---
class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mail_messages/create_mailing.html"
    success_url = reverse_lazy("mail_messages:list_mailing")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = "mail_messages/list_mailing.html"
    context_object_name = "objects_list"

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name="Moderator").exists():
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = "mail_messages/detail_mailing.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()
        return obj


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    template_name = "mail_messages/update_mailing.html"

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name="Moderator").exists():
            return MailingModeratorForm
        return MailingForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.groups.filter(name="Moderator").exists():
            obj.is_moderated = False
        obj.update_status()
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("mail_messages:detail_mailing", kwargs={"pk": self.object.pk})


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = "mail_messages/confirm_delete_mailing.html"
    success_url = reverse_lazy("mail_messages:list_mailing")
