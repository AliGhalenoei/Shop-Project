from django.db import models

from accounts.models import User
from content.models import Product
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
    

class CommentProduct(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='com_users')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='com_products')
    reply = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='com_replys',
        null=True,
        blank=True
    )
    is_reply = models.BooleanField(default=False)
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name = "افزودن بلاگ "
        # verbose_name_plural = "بلاگ ها"
        ordering = ['-id']

    def str(self):
     return f'{self.user} commented {self.message}'
    
class ContactUs(models.Model):

    SUBJECT = (
        ('a','پشتیبانی فنی'),
        ('b','سوالات درباره محصولات'),
        ('c','مشکلات حساب کاربران'),
        ('d','نظرات و پیشنهادات'),
        ('e','شکایت و انتقاد'),
        ('f','همکاری و شراکت'),
        ('g','درخواست اطلاعات بیشتر'),
        ('h','پرسش‌های عمومی')
    )

    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_contact')
    email =models.EmailField(max_length=255 , null=True , blank=True)
    subject = models.CharField(max_length=255 , choices=SUBJECT)
    message = models.TextField()
    is_reply = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.message

class ReplyContact(models.Model):
    user = models.ForeignKey(
        User ,
        on_delete=models.CASCADE ,
        limit_choices_to={'is_admin':True} ,
        related_name='reply_contact'
    )
    contact = models.ForeignKey(ContactUs , on_delete=models.CASCADE , related_name='contacts')
    message = models.TextField()


    