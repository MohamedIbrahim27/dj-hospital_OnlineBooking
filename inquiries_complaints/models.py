from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

class inquiries(models.Model):
    username=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=20,verbose_name=_("phonenumber"))
    message=models.CharField(max_length=1000)


    class Meta:
        verbose_name = _("inquiries")
        verbose_name_plural = _("inquiriss")

    def __str__(self):
        return 'name : ' + self.username + ' <== phonenumber ==> ' + self.phonenumber

    # def get_absolute_url(self):
    #     return reverse("inquiries_detail", kwargs={"pk": self.pk})
