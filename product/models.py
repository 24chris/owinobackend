# from distutils.command.upload import upload
# from email.mime import image
# from unicodedata import category, name
from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slider_image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    slider_image2 = models.ImageField(upload_to='uploads/',blank=True,null=True)
    slider_image3 = models.ImageField(upload_to='uploads/',blank=True,null=True)
    slider_image4 = models.ImageField(upload_to='uploads/',blank=True,null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_slider_image(self):
        if self.slider_image:
            return 'https://owinotest.herokuapp.com' + self.slider_image.url
        return''
    
    def get_slider_image2(self):
        if self.slider_image:
            return 'https://owinotest.herokuapp.com' + self.slider_image2.url
        return''
    
    def get_slider_image3(self):
        if self.slider_image:
            return 'https://owinotest.herokuapp.com' + self.slider_image3.url
        return''
    
    def get_slider_image4(self):
        if self.slider_image:
            return 'https://owinotest.herokuapp.com' + self.slider_image4.url
        return''

    def get_absolute_url(self):
        return f'{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null = True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null = True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'https://owinotest.herokuapp.com' + self.image.url
        return''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'https://owinotest.herokuapp.com' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'https://owinotest.herokuapp.com' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self,image,size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io,'JPEG', quality=85)

        thumbnail = File(thumb_io,name=image.name)

        return thumbnail