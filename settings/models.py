from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class settings(models.Model):
    logo=models.ImageField(upload_to='logo/')
    phoennumbers=models.CharField(max_length=100)
    adress=models.CharField(max_length=150)
    fb_url=models.URLField()
    tw_url=models.URLField()

    class Meta:
        verbose_name = _("settings")
        verbose_name_plural = _("settings")

    # def __str__(self):
    #     return self.site_name

    # def get_absolute_url(self):
    #     return reverse("settings_detail", kwargs={"pk": self.pk})
