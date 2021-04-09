from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Brand(models.Model):
    BrnName = models.CharField( max_length=50)
    BrnDesc = models.TextField(blank=True , null=True)
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return str(self.BrnName)

class Variant(models.Model):
    VerName = models.CharField( max_length=50)
    VerDesc = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return str(self.VerName)

   


    
