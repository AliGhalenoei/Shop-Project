from django.db import models

from accounts.models import User
# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=255 , null=True , blank=True)
    media = models.FileField(upload_to='storys/')

    class Meta:
        verbose_name = "افزودن داستان"
        verbose_name_plural = "داستان ها"
        ordering = ['-id']

    def __str__(self) -> str:
        if self.title:
            return self.title
        return self.id
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "افزودن برچسب "
        verbose_name_plural = "برچسب ها"
        ordering = ['-id']

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'is_admin':True})
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50,unique=True , null=True , blank=True)
    
    class Meta:
        verbose_name = "افزودن بلاگ "
        verbose_name_plural = "بلاگ ها"
        ordering = ['-id']

    def str(self):
     return self.title
    


    