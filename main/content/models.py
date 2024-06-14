from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255 , null=True , blank=True)
    baner= models.ImageField(upload_to='baner_category',null=True,blank=True)
    
    sub = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_category',
        null=True,
        blank=True
    )
    is_sub = models.BooleanField(default=False)

    slug = models.SlugField(unique=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category,related_name='product_category')
    body = models.TextField()
    baner = models.ImageField(upload_to='baner_products/')
    price = models.IntegerField()
    is_avalable=models.BooleanField(default=True)

    slug = models.SlugField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
 
    
class GaleryProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='galery')
    image = models.ImageField(upload_to='galery_products/')
    