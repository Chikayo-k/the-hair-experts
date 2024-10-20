from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    For User profile (delivery info and order history)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    default_eircode = models.CharField(max_length=15, null=True, blank=True)
    default_address1 = models.CharField(max_length=50, null=True, blank=True)
    default_address2 = models.CharField(max_length=50, null=True, blank=True)
    default_town_city = models.CharField(max_length=50, null=True, blank=True)
    default_county_region = models.CharField(max_length=50,
                                             null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()
