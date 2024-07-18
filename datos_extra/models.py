from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define tu modelo UserProfile y asegúrate de tener un campo OneToOneField con User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_info = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)  # Nuevo campo de email

    def __str__(self):
        return self.user.username

# Signal para crear un UserProfile cuando se crea un usuario

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
