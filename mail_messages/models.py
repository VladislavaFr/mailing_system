from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class CustomMessage(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mailings")
    is_moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Черновик")  # "Черновик", "Отправлено", "В процессе"

    def update_status(self):
        # Здесь можно добавить логику проверки отправки
        if self.is_moderated:
            self.status = "Отправлено"
        else:
            self.status = "Черновик"
        self.save()

    def __str__(self):
        return self.name

    @staticmethod
    def get_user_stats(user):
        return {
            "messages_count": CustomMessage.objects.filter(owner=user).count(),
            "mailings_count": Mailing.objects.filter(owner=user).count(),
        }
