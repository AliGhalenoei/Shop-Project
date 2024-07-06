from django.db import models

# Create your models here.


class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    baner= models.ImageField(upload_to='baner_sub_category',null=True,blank=True)

    slug = models.SlugField(unique=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "زیر دسته بندی"
        verbose_name_plural = "زیر دسته بندی ها"


class Category(models.Model):
    title = models.CharField(max_length=255 , null=True , blank=True)
    baner= models.ImageField(upload_to='baner_category',null=True,blank=True)
    
    slug = models.SlugField(unique=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


    def __str__(self) -> str:
        return self.title


class Product(models.Model):

    STATUS_PRODUCT = (
        ('off','تخفیف'),
        ('definite','مقطوع')
    )

    title = models.CharField(max_length = 255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product_category',null=True , blank=True)
    sub_category= models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='sub_category',null=True , blank=True)
    body = models.TextField()
    baner = models.ImageField(upload_to='baner_products/')
    price = models.IntegerField()
    status = models.CharField(max_length=12 , choices=STATUS_PRODUCT , default='definite')
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
    