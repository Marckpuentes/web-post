from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    category = models.CharField(verbose_name="Categoria", max_length=20)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['category']
        
    def __str__(self):
        return self.category


def custom_upload_to(instance, filename):
    #borra la imagen actual que esta guardada y guarda la nueva
    old_intance = CreatePost.objects.get(pk=instance.pk)
    old_intance.img.delete()
    return 'post/'+filename

class CreatePost(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    title = models.CharField(verbose_name="Titulo", max_length=100)
    slug = models.CharField(max_length=200, blank=True)
    content = models.TextField(verbose_name="Contenido", null=True, blank=True)
    img = models.ImageField(upload_to=custom_upload_to, null=True, blank=False)
    category = models.ManyToManyField(Categories)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(CreatePost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'
        ordering = ['-created']        