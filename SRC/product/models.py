from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.files import ImageFieldFile
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Product (models.Model):
    PrdName= models.CharField(verbose_name=_('Product Name'), max_length=50)
    PrdCategory = models.ForeignKey("Category",  on_delete=models.CASCADE, blank= True, null= True, verbose_name=_('Catogery Name'))
    PrdBrand = models.ForeignKey('settings.Brand',  on_delete=models.CASCADE, blank= True, null= True, verbose_name=_('Brand Name'))
    PrdDesc = models.TextField(verbose_name=_('Product Description'))
    PrdImage = models.ImageField(verbose_name=_('imge'), upload_to='media', blank = True,  null= True)
    PrdPrice = models.DecimalField(verbose_name=_('Product Price'), max_digits=8, decimal_places=2)
    PrdDescountPrice = models.DecimalField(verbose_name=_('Product Descount Price'), max_digits=8, decimal_places=2)
    PrdCost = models.DecimalField(verbose_name=_('Product Cost'), max_digits=8, decimal_places=2)
    PrdCreated = models.DateTimeField(verbose_name=_('Product Created'))
    Prdslug= models.SlugField(blank=True, null= True)
      

    
    def save(self, *args, **kwargs):
        if not self.Prdslug:
            self.Prdslug = slugify(self.PrdName)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.Prdslug})
    

    


    def __str__(self):
        return str(self.PrdName)

class ProductImage (models.Model):
    PrdIProduct = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    ProImage = models.ImageField(verbose_name=_('imge'), upload_to='media')    

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return str(self.PrdIProduct)

    
class Category (models.Model):
    CatName = models.CharField(max_length=50, verbose_name = _("Category Name"))
    CatParent = models.ForeignKey('self', on_delete=models.CASCADE,limit_choices_to={'CatParent__isnull':True}, blank = True, null = True, verbose_name = _("Main Category"))
    CatDesc = models.TextField(verbose_name= (" Category Description"))
    CatImg = models.ImageField(upload_to = 'category/', verbose_name = _("Category Image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categoreis")

    def __str__(self):
        return str(self.CatName)

class ProductAlternative(models.Model):
    ProAlnProduct = models.ForeignKey(Product,  related_name='main_product', on_delete=models.CASCADE, verbose_name = _("Product"))
    proAlAlternative = models.ManyToManyField(Product,related_name='alternative_product', verbose_name = _("Alternative"))
    
    class Meta:
        verbose_name = _("Alternative")
        verbose_name_plural = _("Alternatives")
 
    def __str__(self):
        return str(self.ProAlnProduct)

    
class  ParoductAccessories(models.Model):
    PrAccProduct = models.ForeignKey(Product, related_name="main_Accessories", on_delete=models.CASCADE,verbose_name = _("Product"))
    ParAccessories = models.ManyToManyField(Product,related_name='Accessories_product', verbose_name=_("Accessories"))
    

    class Meta:
        verbose_name = _("Accessory")
        verbose_name_plural = _("Accessories")

    def __str__(self):
        return str(self.PrAccProduct)

    

    

    

    



