from django.db import models


class ProfileModel(models.Model):
    name = models.CharField(max_length=10)
    about_yourself = models.TextField()
