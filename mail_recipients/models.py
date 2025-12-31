from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomMailRecipient(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipients")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
