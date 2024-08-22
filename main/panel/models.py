from django.db import models

# Create your models here.


class MenuNavbar(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.title