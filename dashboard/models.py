from django.db import models

# Create your models here.

class dealerinfo(models.Model):
    organization_name = models.CharField(max_length=255)
    product_category = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gst_number = models.IntegerField()
    personal_email = models.EmailField()
    company_email = models.EmailField()
    personal_phone = models.IntegerField()
    organization_phone = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.organization_name
