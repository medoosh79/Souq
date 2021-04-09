from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(_("image"), upload_to='profile_img', blank= True, null= True)
    country = CountryField()
    Address = models.CharField( max_length=150)
    join_date = models.DateTimeField(_("join date"), default= datetime.datetime.now())
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs) 

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})


def crate_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user= kwargs['instance'])


post_save.connect(crate_profile, sender=User)
