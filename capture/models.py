from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=100)
   

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
        
class photos(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    category = models.ForeignKey(categories , blank=True, null=True, on_delete=models.CASCADE)

class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    msg = models.CharField(max_length=250)
    
    
class adminuser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
