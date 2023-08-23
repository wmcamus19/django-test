from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Agent (models.Model):
    """Model definition for Agent."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Agent."""

        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        """Unicode representation of Agent."""
        return f"{self.user}"


class Lead (models.Model):
    """Model definition for Lead."""

    # TODO: Define fields here
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Lead."""

        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        """Unicode representation of Lead."""
        return f"{self.first_name} {self.last_name}"


# class Lead (models.Model):

#     SOURCE_CHOICES = (
#         ('Youtube', 'Youtube'),
#         ('Google', 'Google'),
#         ('Newsletter', 'Newsletter'),
#     )

#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     age = models.IntegerField(default=0)

#     phoned = models.BooleanField(default=False)
#     source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

#     profile_picture = models.ImageField(blank=True, null=True)
#     special_files = models.FileField(blank=True, null=True)
