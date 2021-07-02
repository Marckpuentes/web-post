from django.db import models
from post.models import CreatePost
# Create your models here.

def custom_upload_to(instance, filename):
    #borra la imagen actual que esta guardada y guarda la nueva
    #old_intance = CreatePost.objects.get(pk=instance.pk)
    #old_intance.img.delete()
    return 'cap/'+filename


class Cap(models.Model):
    title = models.ForeignKey(CreatePost, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=custom_upload_to, null=True, blank=False)
    numeroCapitulo = models.CharField(verbose_name="Numero Capitulo", max_length=50, null=True, blank=True)
    cap = models.FileField(upload_to=custom_upload_to, verbose_name="Video", null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
        ordering = ['-created', 'title']
