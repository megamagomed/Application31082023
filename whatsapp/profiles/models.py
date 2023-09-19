from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    name = models.CharField(max_length=10)
    about_yourself = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class MessageModel(models.Model):
    
    message = models.TextField()
    sender = models.ForeignKey(
        User, related_name="sender_user", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name="receiver_user", on_delete=models.CASCADE
    )
