from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

#instance hace referencia al objeto que se esta guardando 
#pero despues de que se haya confirmado el nuevo valir
def custom_upload_to(instance, filename):
    old_intance = Profile.objects.get(pk=instance.pk)
    old_intance.avatar.delete()
    return 'profile/'+filename

class Profile(models.Model):
    #relacionando el usuario con un perfil en bd
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

#ejecutar despues de que se guarde el usuario
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        #print("se acaba de crear un usuario y su perfil enlazado")