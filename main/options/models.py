from django.db import models

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
    
    